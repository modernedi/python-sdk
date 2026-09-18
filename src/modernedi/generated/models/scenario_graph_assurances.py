# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioGraphAssurances(BaseModel):
    """
    Only assurances declared by this step are present. Pending evidence can be refreshed by observing the same transaction again with a new command identity.
    """ # noqa: E501
    mapping_succeeded: Optional[StrictStr] = None
    transport_receipt_accepted: Optional[StrictStr] = None
    interchange_acknowledgment_accepted: Optional[StrictStr] = None
    functional_or_implementation_acknowledgment_accepted: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["mapping_succeeded", "transport_receipt_accepted", "interchange_acknowledgment_accepted", "functional_or_implementation_acknowledgment_accepted"]

    @field_validator('mapping_succeeded')
    def mapping_succeeded_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['pending', 'passed', 'failed']):
            raise ValueError("must be one of enum values ('pending', 'passed', 'failed')")
        return value

    @field_validator('transport_receipt_accepted')
    def transport_receipt_accepted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['pending', 'passed', 'failed']):
            raise ValueError("must be one of enum values ('pending', 'passed', 'failed')")
        return value

    @field_validator('interchange_acknowledgment_accepted')
    def interchange_acknowledgment_accepted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['pending', 'passed', 'failed']):
            raise ValueError("must be one of enum values ('pending', 'passed', 'failed')")
        return value

    @field_validator('functional_or_implementation_acknowledgment_accepted')
    def functional_or_implementation_acknowledgment_accepted_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['pending', 'passed', 'failed']):
            raise ValueError("must be one of enum values ('pending', 'passed', 'failed')")
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
        """Create an instance of ScenarioGraphAssurances from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioGraphAssurances from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "mapping_succeeded": obj.get("mapping_succeeded"),
            "transport_receipt_accepted": obj.get("transport_receipt_accepted"),
            "interchange_acknowledgment_accepted": obj.get("interchange_acknowledgment_accepted"),
            "functional_or_implementation_acknowledgment_accepted": obj.get("functional_or_implementation_acknowledgment_accepted")
        }.items() if key in obj})
        return _obj
