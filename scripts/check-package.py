"""Public, stdlib-only artifact and registry checks. Never uploads or reads credentials."""
import argparse
import email
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import tarfile
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def package_identity(root, language):
    manifest = json.loads((root / "PUBLIC_SOURCE.json").read_text(encoding="utf-8"))
    name, repository = (("modernedi-sdk", "modernedi/python-sdk") if language == "python"
                        else ("ModernEdi", "modernedi/dotnet-sdk"))
    require(manifest["package"] == name and manifest["repository"] == repository, "Unexpected publisher identity")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Expected exact package version")
    return manifest["version"], repository


def safe_names(names):
    require(len(names) == len(set(names)), "Duplicate archive entries")
    for name in names:
        require(not name.startswith("/") and "\\" not in name and ".." not in PurePosixPath(name).parts,
                "Unsafe archive path")
        require(not any(part in {".git", ".env", "codegen", "node_modules", "__pycache__"}
                        for part in PurePosixPath(name).parts), "Private or generated cache in package")


def zip_entries(data):
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        safe_names(archive.namelist())
        require(all((entry.external_attr >> 16) & 0o170000 != 0o120000 for entry in archive.infolist()),
                "Archive symlink")
        return {entry.filename: archive.read(entry) for entry in archive.infolist() if not entry.is_dir()}


def validate_python_metadata(data, version):
    metadata = email.message_from_bytes(data)
    require(metadata["Name"] == "modernedi-sdk" and metadata["Version"] == version, "Wrong Python package identity")
    require("Source, https://github.com/modernedi/python-sdk" in metadata.get_all("Project-URL", []),
            "Missing public Python repository metadata")


def validate_artifacts(root, language, allow_attestations=False):
    version, repository = package_identity(root, language)
    expected = ([f"modernedi_sdk-{version}-py3-none-any.whl", f"modernedi_sdk-{version}.tar.gz"]
                if language == "python" else [f"ModernEdi.{version}.nupkg"])
    artifacts = {file.name: file.read_bytes() for file in (root / "dist").iterdir() if file.is_file()}
    if allow_attestations and language == "python":
        # The official PyPI action creates these sidecars during publication. They are
        # not extra distributions, and are not allowed in the pre-upload inventory.
        artifacts = {name: data for name, data in artifacts.items()
                     if name not in {f"{package}.publish.attestation" for package in expected}}
    require(set(artifacts) == set(expected), "Unexpected or missing package artifacts")
    for name, data in artifacts.items():
        if name.endswith(".whl"):
            entries = zip_entries(data)
            validate_python_metadata(entries[f"modernedi_sdk-{version}.dist-info/METADATA"], version)
            require("modernedi/py.typed" in entries and "modernedi/generated/contract.json" in entries,
                    "Missing typed Python client or contract")
            require(all(key.startswith(("modernedi/", f"modernedi_sdk-{version}.dist-info/")) for key in entries),
                    "Unexpected wheel content")
        elif name.endswith(".tar.gz"):
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
                members = archive.getmembers()
                safe_names([member.name for member in members])
                require(all(member.isfile() or member.isdir() for member in members), "Source archive links are forbidden")
                prefix = f"modernedi_sdk-{version}/"
                require(all(member.name.startswith(prefix) for member in members), "Unexpected sdist root")
                require(all(member.name[len(prefix):].split('/')[0] in
                            {"src", "tests", "examples", "README.md", "LICENSE", "pyproject.toml", "PKG-INFO", ".gitignore"}
                            for member in members), "Unexpected source package content")
                validate_python_metadata(archive.extractfile(prefix + "PKG-INFO").read(), version)
        else:
            entries = zip_entries(data)
            nuspecs = [value for key, value in entries.items() if key.endswith(".nuspec")]
            require(len(nuspecs) == 1, "Expected one NuGet manifest")
            metadata = ET.fromstring(nuspecs[0]).find("{*}metadata")
            require(metadata.findtext("{*}id") == "ModernEdi" and metadata.findtext("{*}version") == version,
                    "Wrong NuGet package identity")
            require(metadata.find("{*}repository").get("url") == f"https://github.com/{repository}",
                    "Wrong NuGet repository")
            require({"lib/net8.0/ModernEdi.dll", "lib/net8.0/ModernEdi.xml", "README.md"} <= entries.keys(),
                    "Missing .NET assembly, XML documentation, or README")
            require(not any(key.endswith((".cs", ".csproj", ".pdb")) for key in entries), "Unexpected NuGet source content")
    return artifacts


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "ModernEDI-package-verification"}), timeout=30) as response:
            return response.read()
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise


def registry_url(language, version):
    return (f"https://pypi.org/pypi/modernedi-sdk/{version}/json" if language == "python" else
            f"https://api.nuget.org/v3-flatcontainer/modernedi/{version}/modernedi.{version}.nupkg")


def preflight(root, language, fetch=get):
    validate_artifacts(root, language)
    version, _ = package_identity(root, language)
    contract_path = ("src/modernedi/generated/contract.json" if language == "python" else "src/ModernEdi/Generated/contract.json")
    contract = json.loads((root / contract_path).read_text(encoding="utf-8"))
    for host in ["www.modernedi.com", "app.modernedi.com"]:
        spec = fetch(f"https://{host}/integration-api/openapi.yaml")
        require(spec is not None and hashlib.sha256(spec.replace(b"\r\n", b"\n")).hexdigest() == contract["bundledSpecificationSha256"],
                f"SDK differs from the deployed API contract on {host}")
    require(fetch(registry_url(language, version)) is None,
            "Version already exists: inspect the prior publication; never blindly upload again")


def verify_registry(root, language, data):
    artifacts = validate_artifacts(root, language, allow_attestations=True)
    if language == "python":
        published = {item["filename"]: item for item in json.loads(data)["urls"]}
        require(set(published) == set(artifacts), "Registry artifact inventory differs")
        for name, content in artifacts.items():
            require(not published[name]["yanked"], "Registry artifact is yanked")
            require(published[name]["digests"]["sha256"] == hashlib.sha256(content).hexdigest(), "Registry digest differs")
    else:
        local = zip_entries(next(iter(artifacts.values())))
        remote = zip_entries(data)
        # NuGet repository-signs uploads. Signature bytes/content-type registration can differ;
        # every payload, manifest, and assembly must still match the reviewed local artifact.
        ignored = {".signature.p7s", "[Content_Types].xml"}
        require({key: value for key, value in local.items() if key not in ignored} ==
                {key: value for key, value in remote.items() if key not in ignored}, "NuGet package payload differs")
        require(".signature.p7s" in remote, "Missing NuGet repository signature")
        directory = root / "registry"
        directory.mkdir(exist_ok=True)
        (directory / next(iter(artifacts))).write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["check", "preflight", "registry"])
    parser.add_argument("language", choices=["python", "dotnet"])
    args = parser.parse_args()
    root = Path.cwd()
    if args.action == "check":
        validate_artifacts(root, args.language)
    elif args.action == "preflight":
        preflight(root, args.language)
    else:
        version, _ = package_identity(root, args.language)
        deadline = time.monotonic() + 600
        while True:
            data = get(registry_url(args.language, version))
            if data is not None:
                verify_registry(root, args.language, data)
                break
            require(time.monotonic() < deadline, "Registry visibility timed out; inspect before retrying publication")
            time.sleep(20)
    print(f"Verified {args.language} {args.action}.")


if __name__ == "__main__":
    main()
