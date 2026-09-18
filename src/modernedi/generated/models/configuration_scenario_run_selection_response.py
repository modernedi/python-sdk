# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from modernedi.generated.models.start_scenario_run_request import StartScenarioRunRequest
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioRunSelectionResponse(BaseModel):
    """
    Exact run-start selectors for an active authored binding in the specified completed configuration snapshot. This does not attest runtime availability or run success.
    """ # noqa: E501
    success: StrictBool
    configuration_apply_operation_id: Annotated[str, Field(strict=True)] = Field(description="The requested apply operation, not a substituted latest operation.", alias="configurationApplyOperationId")
    applied_snapshot_etag: Annotated[str, Field(strict=True)] = Field(description="Matches the requested apply's appliedSnapshotEtag. Not a scenario-run revision ETag.", alias="appliedSnapshotEtag")
    selection: StartScenarioRunRequest
    __properties: ClassVar[List[str]] = ["success", "configurationApplyOperationId", "appliedSnapshotEtag", "selection"]

    @field_validator('configuration_apply_operation_id', mode="before")
    def configuration_apply_operation_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^apply-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(r"must validate the regular expression /^apply-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/")
        return value

    @field_validator('applied_snapshot_etag', mode="before")
    def applied_snapshot_etag_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\"[0-9a-f]{64}\"$", value):
            raise ValueError(r"must validate the regular expression /^\"[0-9a-f]{64}\"$/")
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
        """Create an instance of ConfigurationScenarioRunSelectionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of selection
        if self.selection:
            _dict['selection'] = self.selection.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioRunSelectionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "configurationApplyOperationId": obj.get("configurationApplyOperationId"),
            "appliedSnapshotEtag": obj.get("appliedSnapshotEtag"),
            "selection": StartScenarioRunRequest.from_dict(obj["selection"]) if obj.get("selection") is not None else None
        }.items() if key in obj})
        return _obj
