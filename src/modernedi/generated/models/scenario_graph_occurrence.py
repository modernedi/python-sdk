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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.scenario_graph_assurances import ScenarioGraphAssurances
from modernedi.generated.models.scenario_graph_evidence_reference import ScenarioGraphEvidenceReference
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioGraphOccurrence(BaseModel):
    """
    ScenarioGraphOccurrence
    """ # noqa: E501
    occurrence: Annotated[int, Field(strict=True, ge=1)]
    observed_at: str = Field(alias="observedAt")
    message_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="messageId")
    transaction_key: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="transactionKey")
    reply_to_message_id: Optional[StrictStr] = Field(alias="replyToMessageId")
    reply_to_transaction_key: Optional[StrictStr] = Field(alias="replyToTransactionKey")
    direction: StrictStr
    partner_id: Annotated[int, Field(strict=True, ge=1)] = Field(alias="partnerId")
    transaction_set: Annotated[str, Field(strict=True)] = Field(alias="transactionSet")
    x12_version: Annotated[str, Field(strict=True)] = Field(description="Canonical six-digit public X12 release identity.", alias="x12Version")
    mapping_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(alias="mappingId")
    assurances: ScenarioGraphAssurances
    evidence: List[ScenarioGraphEvidenceReference]
    __properties: ClassVar[List[str]] = ["occurrence", "observedAt", "messageId", "transactionKey", "replyToMessageId", "replyToTransactionKey", "direction", "partnerId", "transactionSet", "x12Version", "mappingId", "assurances", "evidence"]

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['incoming', 'outgoing']):
            raise ValueError("must be one of enum values ('incoming', 'outgoing')")
        return value

    @field_validator('transaction_set', mode="before")
    def transaction_set_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9]{3}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{3}$/")
        return value

    @field_validator('x12_version', mode="before")
    def x12_version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9]{6}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{6}$/")
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
        """Create an instance of ScenarioGraphOccurrence from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of assurances
        if self.assurances:
            _dict['assurances'] = self.assurances.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in evidence (list)
        _items = []
        if self.evidence:
            for _item_evidence in self.evidence:
                if _item_evidence:
                    _items.append(_item_evidence.to_dict())
            _dict['evidence'] = _items
        # set to None if reply_to_message_id (nullable) is None
        # and model_fields_set contains the field
        if self.reply_to_message_id is None and "reply_to_message_id" in self.model_fields_set:
            _dict['replyToMessageId'] = None

        # set to None if reply_to_transaction_key (nullable) is None
        # and model_fields_set contains the field
        if self.reply_to_transaction_key is None and "reply_to_transaction_key" in self.model_fields_set:
            _dict['replyToTransactionKey'] = None

        # set to None if mapping_id (nullable) is None
        # and model_fields_set contains the field
        if self.mapping_id is None and "mapping_id" in self.model_fields_set:
            _dict['mappingId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioGraphOccurrence from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "occurrence": obj.get("occurrence"),
            "observedAt": obj.get("observedAt"),
            "messageId": obj.get("messageId"),
            "transactionKey": obj.get("transactionKey"),
            "replyToMessageId": obj.get("replyToMessageId"),
            "replyToTransactionKey": obj.get("replyToTransactionKey"),
            "direction": obj.get("direction"),
            "partnerId": obj.get("partnerId"),
            "transactionSet": obj.get("transactionSet"),
            "x12Version": obj.get("x12Version"),
            "mappingId": obj.get("mappingId"),
            "assurances": ScenarioGraphAssurances.from_dict(obj["assurances"]) if obj.get("assurances") is not None else None,
            "evidence": [ScenarioGraphEvidenceReference.from_dict(_item) for _item in obj["evidence"]] if obj.get("evidence") is not None else None
        }.items() if key in obj})
        return _obj
