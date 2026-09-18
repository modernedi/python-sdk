# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_external_repository_import_verification import ConfigurationExternalRepositoryImportVerification
from modernedi.generated.models.configuration_external_repository_last_error import ConfigurationExternalRepositoryLastError
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationExternalRepository(BaseModel):
    """
    ConfigurationExternalRepository
    """ # noqa: E501
    repository_url: StrictStr = Field(description="Canonical HTTPS repository URL without credentials.", alias="repositoryUrl")
    branch: StrictStr
    directory: StrictStr = Field(description="Bundle directory within the connected repository.")
    status: StrictStr = Field(description="Current synchronization state. Held means import tests have not authorized an import; conflict means both sides changed and an owner must review.")
    automatic: StrictBool
    verify_before_import: StrictBool = Field(alias="verifyBeforeImport")
    import_verification: Optional[ConfigurationExternalRepositoryImportVerification] = Field(alias="importVerification")
    revision: Annotated[int, Field(strict=True, ge=0)] = Field(description="Connection status revision; polling may advance it without a configuration change.")
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    next_attempt_at: str = Field(description="Scheduled check or retry time; not a completion promise.", alias="nextAttemptAt")
    last_synced_at: Optional[str] = Field(alias="lastSyncedAt")
    workspace_commit_sha: Optional[Annotated[str, Field(strict=True)]] = Field(description="Last synchronized internal workspace Git commit.", alias="workspaceCommitSha")
    repository_commit_sha: Optional[Annotated[str, Field(strict=True)]] = Field(description="Last synchronized external commit; may differ from the remote branch's current HEAD.", alias="repositoryCommitSha")
    last_error: Optional[ConfigurationExternalRepositoryLastError] = Field(alias="lastError")
    __properties: ClassVar[List[str]] = ["repositoryUrl", "branch", "directory", "status", "automatic", "verifyBeforeImport", "importVerification", "revision", "createdAt", "updatedAt", "nextAttemptAt", "lastSyncedAt", "workspaceCommitSha", "repositoryCommitSha", "lastError"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pending', 'syncing', 'synced', 'conflict', 'held', 'error']):
            raise ValueError("must be one of enum values ('pending', 'syncing', 'synced', 'conflict', 'held', 'error')")
        return value

    @field_validator('workspace_commit_sha', mode="before")
    def workspace_commit_sha_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[0-9a-f]{40}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{40}$/")
        return value

    @field_validator('repository_commit_sha', mode="before")
    def repository_commit_sha_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[0-9a-f]{40}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{40}$/")
        return value

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ConfigurationExternalRepository from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_unset=True,
        )
        # override the default output from pydantic by calling `to_dict()` of import_verification
        if self.import_verification:
            _dict['importVerification'] = self.import_verification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_error
        if self.last_error:
            _dict['lastError'] = self.last_error.to_dict()
        # set to None if import_verification (nullable) is None
        # and model_fields_set contains the field
        if self.import_verification is None and "import_verification" in self.model_fields_set:
            _dict['importVerification'] = None

        # set to None if last_synced_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_synced_at is None and "last_synced_at" in self.model_fields_set:
            _dict['lastSyncedAt'] = None

        # set to None if workspace_commit_sha (nullable) is None
        # and model_fields_set contains the field
        if self.workspace_commit_sha is None and "workspace_commit_sha" in self.model_fields_set:
            _dict['workspaceCommitSha'] = None

        # set to None if repository_commit_sha (nullable) is None
        # and model_fields_set contains the field
        if self.repository_commit_sha is None and "repository_commit_sha" in self.model_fields_set:
            _dict['repositoryCommitSha'] = None

        # set to None if last_error (nullable) is None
        # and model_fields_set contains the field
        if self.last_error is None and "last_error" in self.model_fields_set:
            _dict['lastError'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationExternalRepository from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "repositoryUrl": obj.get("repositoryUrl"),
            "branch": obj.get("branch"),
            "directory": obj.get("directory"),
            "status": obj.get("status"),
            "automatic": obj.get("automatic"),
            "verifyBeforeImport": obj.get("verifyBeforeImport"),
            "importVerification": ConfigurationExternalRepositoryImportVerification.from_dict(obj["importVerification"]) if obj.get("importVerification") is not None else None,
            "revision": obj.get("revision"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "nextAttemptAt": obj.get("nextAttemptAt"),
            "lastSyncedAt": obj.get("lastSyncedAt"),
            "workspaceCommitSha": obj.get("workspaceCommitSha"),
            "repositoryCommitSha": obj.get("repositoryCommitSha"),
            "lastError": ConfigurationExternalRepositoryLastError.from_dict(obj["lastError"]) if obj.get("lastError") is not None else None
        }.items() if key in obj})
        return _obj
