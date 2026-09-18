"""Read-only example: export and plan the same configuration; never apply or send EDI."""
import os
from modernedi import ModernEdiClient, models


def main():
    with ModernEdiClient(api_key=os.environ["MODERNEDI_API_KEY"]) as client:
        exported = client.configuration_as_code.export_integration_configuration()
        if exported.data is None:
            raise RuntimeError("Expected an unconditional configuration export")
        request = models.ConfigurationPlanRequest.from_dict({"files": exported.data.to_dict()["files"]})
        result = client.configuration_as_code.plan_integration_configuration(body=request)
        print(f"Plan completed; support request ID: {result.request_id}")


if __name__ == "__main__":
    main()
