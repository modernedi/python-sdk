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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceOccurrence(BaseModel):
    """
    ScenarioEvidenceOccurrence
    """ # noqa: E501
    occurrence: Annotated[int, Field(strict=True, ge=1)]
    observed_at: str = Field(alias="observedAt")
    message_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="messageId")
    transaction_key: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="transactionKey")
    partner_id: Annotated[int, Field(strict=True, ge=1)] = Field(alias="partnerId")
    mapping_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(alias="mappingId")
    __properties: ClassVar[List[str]] = ["occurrence", "observedAt", "messageId", "transactionKey", "partnerId", "mappingId"]

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
        """Create an instance of ScenarioEvidenceOccurrence from a JSON string"""
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
        # set to None if mapping_id (nullable) is None
        # and model_fields_set contains the field
        if self.mapping_id is None and "mapping_id" in self.model_fields_set:
            _dict['mappingId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceOccurrence from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "occurrence": obj.get("occurrence"),
            "observedAt": obj.get("observedAt"),
            "messageId": obj.get("messageId"),
            "transactionKey": obj.get("transactionKey"),
            "partnerId": obj.get("partnerId"),
            "mappingId": obj.get("mappingId")
        }.items() if key in obj})
        return _obj
