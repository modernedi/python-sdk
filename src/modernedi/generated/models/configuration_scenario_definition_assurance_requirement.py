# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionAssuranceRequirement(BaseModel):
    """
    One observable proof required for a step. For example, mapping_succeeded proves that the selected map ran, while functional_or_implementation_acknowledgment_accepted proves accepted 997 or 999 evidence. Outgoing mapping proof may predate the document occurrence because mapping runs immediately before exchange; receipts and acknowledgments may not. A deadline is measured from the document occurrence to the terminal evidence time, and requires that evidence's own timestamp. Terminal evidence timestamped after the run's evaluation time is invalid.
    """ # noqa: E501
    type: StrictStr = Field(description="mapping_succeeded proves mapper execution; transport_receipt_accepted proves the AS2 receipt; interchange_acknowledgment_accepted proves TA1 acceptance; functional_or_implementation_acknowledgment_accepted proves accepted 997 or 999 evidence.")
    within: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A positive ISO 8601 duration accepted by java.time.Duration, no longer than P365D. Examples: PT30M, PT4H, P2D. The server enforces the upper bound.")
    __properties: ClassVar[List[str]] = ["type", "within"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['mapping_succeeded', 'transport_receipt_accepted', 'interchange_acknowledgment_accepted', 'functional_or_implementation_acknowledgment_accepted']):
            raise ValueError("must be one of enum values ('mapping_succeeded', 'transport_receipt_accepted', 'interchange_acknowledgment_accepted', 'functional_or_implementation_acknowledgment_accepted')")
        return value

    @field_validator('within', mode="before")
    def within_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^P(?=.+)(?!0+(?:D|T(?:0+H)?(?:0+M)?(?:0+(?:\.0+)?S)?$))(?:[0-9]+D)?(?:T(?=[0-9])(?:[0-9]+H)?(?:[0-9]+M)?(?:[0-9]+(?:\.[0-9]+)?S)?)?$", value):
            raise ValueError(r"must validate the regular expression /^P(?=.+)(?!0+(?:D|T(?:0+H)?(?:0+M)?(?:0+(?:\.0+)?S)?$))(?:[0-9]+D)?(?:T(?=[0-9])(?:[0-9]+H)?(?:[0-9]+M)?(?:[0-9]+(?:\.[0-9]+)?S)?)?$/")
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
        """Create an instance of ConfigurationScenarioDefinitionAssuranceRequirement from a JSON string"""
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
        """Create an instance of ConfigurationScenarioDefinitionAssuranceRequirement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "type": obj.get("type"),
            "within": obj.get("within")
        }.items() if key in obj})
        return _obj
