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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.mapping_runtime_transaction_reference import MappingRuntimeTransactionReference
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionMappingAttempt(BaseModel):
    """
    One persisted mapping execution result with source revision, diagnostic location, replay linkage, and resolution state.
    """ # noqa: E501
    correlation_id: StrictStr = Field(description="ModernEDI correlation id for the mapping operation. For a normal transaction-backed attempt this is the AS2 Message-Id. For a pre-transaction outbound failure it is an opaque request correlation id and must not be presented as an AS2 Message-Id. ", alias="correlationId")
    transaction_reference: Optional[MappingRuntimeTransactionReference] = Field(description="Transaction that owns this attempt, or `null` when mapping failed before ModernEDI could create a transaction. ", alias="transactionReference")
    failure_id: Optional[StrictStr] = Field(description="Opaque identifier for correlating and retrieving a failed attempt. This is `null` for successful attempts because the failure-detail endpoint intentionally exposes only retained failures. ", alias="failureId")
    attempt_id: StrictStr = Field(description="Opaque identifier for this individual mapping execution attempt.", alias="attemptId")
    transaction_key: StrictStr = Field(description="Source transaction key shown in the transaction viewer. Pre-transaction outbound failures use the sentinel `outbound-request`; internal mapping-attempt persistence keys are never exposed. ", alias="transactionKey")
    direction: StrictStr = Field(description="Whether this attempt processed inbound X12 or generated outbound X12.")
    environment: TransactionEnvironmentValue
    partner_name: Optional[StrictStr] = Field(default=None, description="Partner name captured at execution time, or `null` when attribution was unavailable.", alias="partnerName")
    partner_id: Optional[StrictInt] = Field(default=None, description="Stable workspace-scoped partner id, or `null` when the attempt could not be attributed.", alias="partnerId")
    mapping_id: Optional[StrictInt] = Field(default=None, description="Workspace-scoped mapping id, or `null` when no published map was resolved.", alias="mappingId")
    map_file: Optional[StrictStr] = Field(default=None, description="Transform filename attempted, or `null` when selection failed before a file was resolved.", alias="mapFile")
    map_file_sha256_hash: Optional[StrictStr] = Field(default=None, description="Base64 SHA-256 hash of the transform source actually attempted, or `null` when unavailable.", alias="mapFileSha256Hash")
    current_map_file_sha256_hash: Optional[StrictStr] = Field(default=None, description="Base64 SHA-256 hash of the currently published source, or `null` when it cannot be resolved.", alias="currentMapFileSha256Hash")
    current_revision: StrictBool = Field(description="Whether the attempted map hash is still the currently published revision.", alias="currentRevision")
    transaction_set_identifier_code: Optional[StrictStr] = Field(default=None, description="ST01 transaction-set identifier associated with the attempt, or `null` when unknown.", alias="transactionSetIdentifierCode")
    transaction_control_number: Optional[StrictStr] = Field(default=None, description="ST02 transaction control number associated with the attempt, or `null` when unknown.", alias="transactionControlNumber")
    functional_identifier_code: Optional[StrictStr] = Field(default=None, description="GS01 functional identifier associated with the attempt, or `null` when unknown.", alias="functionalIdentifierCode")
    functional_group_control_number: Optional[StrictStr] = Field(default=None, description="GS06 functional-group control number associated with the attempt, or `null` when unknown.", alias="functionalGroupControlNumber")
    x12_version: Optional[StrictStr] = Field(default=None, description="X12 implementation version used by the attempt, or `null` when unresolved.", alias="x12Version")
    stage: StrictStr = Field(description="Mapping pipeline stage that produced the result.")
    status: StrictStr = Field(description="Whether this individual mapping attempt succeeded or failed.")
    code: StrictStr = Field(description="Stable machine-readable mapping result code.")
    safe_message: Optional[StrictStr] = Field(default=None, description="Sanitized diagnostic message safe to display to workspace operators.", alias="safeMessage")
    line: Optional[StrictInt] = Field(default=None, description="One-based source line for a transform diagnostic, or `null` when no precise location exists.")
    column: Optional[StrictInt] = Field(default=None, description="One-based source column for a transform diagnostic, or `null` when no precise location exists.")
    fallback: StrictStr = Field(description="Fallback behavior used after this attempt, or `NONE`.")
    timestamp: str = Field(description="UTC instant when this mapping attempt was recorded.")
    replay_id: Optional[StrictStr] = Field(default=None, description="Replay operation id that created this attempt, or `null` for ordinary processing.", alias="replayId")
    replay_of_attempt_id: Optional[StrictStr] = Field(default=None, description="Original failed attempt targeted by this replay, or `null` when the attempt was not a replay.", alias="replayOfAttemptId")
    resolved: StrictBool = Field(description="Whether a later successful attempt has resolved this failure for operator-attention purposes.")
    resolved_at: Optional[str] = Field(default=None, description="UTC instant when the failure was resolved, or `null` while unresolved or not applicable.", alias="resolvedAt")
    resolved_by_attempt_id: Optional[StrictStr] = Field(default=None, description="Successful attempt id that resolved this failure, or `null` while unresolved or not applicable.", alias="resolvedByAttemptId")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["correlationId", "transactionReference", "failureId", "attemptId", "transactionKey", "direction", "environment", "partnerName", "partnerId", "mappingId", "mapFile", "mapFileSha256Hash", "currentMapFileSha256Hash", "currentRevision", "transactionSetIdentifierCode", "transactionControlNumber", "functionalIdentifierCode", "functionalGroupControlNumber", "x12Version", "stage", "status", "code", "safeMessage", "line", "column", "fallback", "timestamp", "replayId", "replayOfAttemptId", "resolved", "resolvedAt", "resolvedByAttemptId"]

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['inbound', 'outbound']):
            raise ValueError("must be one of enum values ('inbound', 'outbound')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['FAILED', 'SUCCEEDED']):
            raise ValueError("must be one of enum values ('FAILED', 'SUCCEEDED')")
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
        """Create an instance of TransactionMappingAttempt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_unset=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transaction_reference
        if self.transaction_reference:
            _dict['transactionReference'] = self.transaction_reference.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if transaction_reference (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_reference is None and "transaction_reference" in self.model_fields_set:
            _dict['transactionReference'] = None

        # set to None if failure_id (nullable) is None
        # and model_fields_set contains the field
        if self.failure_id is None and "failure_id" in self.model_fields_set:
            _dict['failureId'] = None

        # set to None if partner_name (nullable) is None
        # and model_fields_set contains the field
        if self.partner_name is None and "partner_name" in self.model_fields_set:
            _dict['partnerName'] = None

        # set to None if partner_id (nullable) is None
        # and model_fields_set contains the field
        if self.partner_id is None and "partner_id" in self.model_fields_set:
            _dict['partnerId'] = None

        # set to None if mapping_id (nullable) is None
        # and model_fields_set contains the field
        if self.mapping_id is None and "mapping_id" in self.model_fields_set:
            _dict['mappingId'] = None

        # set to None if map_file (nullable) is None
        # and model_fields_set contains the field
        if self.map_file is None and "map_file" in self.model_fields_set:
            _dict['mapFile'] = None

        # set to None if map_file_sha256_hash (nullable) is None
        # and model_fields_set contains the field
        if self.map_file_sha256_hash is None and "map_file_sha256_hash" in self.model_fields_set:
            _dict['mapFileSha256Hash'] = None

        # set to None if current_map_file_sha256_hash (nullable) is None
        # and model_fields_set contains the field
        if self.current_map_file_sha256_hash is None and "current_map_file_sha256_hash" in self.model_fields_set:
            _dict['currentMapFileSha256Hash'] = None

        # set to None if transaction_set_identifier_code (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_set_identifier_code is None and "transaction_set_identifier_code" in self.model_fields_set:
            _dict['transactionSetIdentifierCode'] = None

        # set to None if transaction_control_number (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_control_number is None and "transaction_control_number" in self.model_fields_set:
            _dict['transactionControlNumber'] = None

        # set to None if functional_identifier_code (nullable) is None
        # and model_fields_set contains the field
        if self.functional_identifier_code is None and "functional_identifier_code" in self.model_fields_set:
            _dict['functionalIdentifierCode'] = None

        # set to None if functional_group_control_number (nullable) is None
        # and model_fields_set contains the field
        if self.functional_group_control_number is None and "functional_group_control_number" in self.model_fields_set:
            _dict['functionalGroupControlNumber'] = None

        # set to None if x12_version (nullable) is None
        # and model_fields_set contains the field
        if self.x12_version is None and "x12_version" in self.model_fields_set:
            _dict['x12Version'] = None

        # set to None if safe_message (nullable) is None
        # and model_fields_set contains the field
        if self.safe_message is None and "safe_message" in self.model_fields_set:
            _dict['safeMessage'] = None

        # set to None if line (nullable) is None
        # and model_fields_set contains the field
        if self.line is None and "line" in self.model_fields_set:
            _dict['line'] = None

        # set to None if column (nullable) is None
        # and model_fields_set contains the field
        if self.column is None and "column" in self.model_fields_set:
            _dict['column'] = None

        # set to None if replay_id (nullable) is None
        # and model_fields_set contains the field
        if self.replay_id is None and "replay_id" in self.model_fields_set:
            _dict['replayId'] = None

        # set to None if replay_of_attempt_id (nullable) is None
        # and model_fields_set contains the field
        if self.replay_of_attempt_id is None and "replay_of_attempt_id" in self.model_fields_set:
            _dict['replayOfAttemptId'] = None

        # set to None if resolved_at (nullable) is None
        # and model_fields_set contains the field
        if self.resolved_at is None and "resolved_at" in self.model_fields_set:
            _dict['resolvedAt'] = None

        # set to None if resolved_by_attempt_id (nullable) is None
        # and model_fields_set contains the field
        if self.resolved_by_attempt_id is None and "resolved_by_attempt_id" in self.model_fields_set:
            _dict['resolvedByAttemptId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionMappingAttempt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "correlationId": obj.get("correlationId"),
            "transactionReference": MappingRuntimeTransactionReference.from_dict(obj["transactionReference"]) if obj.get("transactionReference") is not None else None,
            "failureId": obj.get("failureId"),
            "attemptId": obj.get("attemptId"),
            "transactionKey": obj.get("transactionKey"),
            "direction": obj.get("direction"),
            "environment": obj.get("environment"),
            "partnerName": obj.get("partnerName"),
            "partnerId": obj.get("partnerId"),
            "mappingId": obj.get("mappingId"),
            "mapFile": obj.get("mapFile"),
            "mapFileSha256Hash": obj.get("mapFileSha256Hash"),
            "currentMapFileSha256Hash": obj.get("currentMapFileSha256Hash"),
            "currentRevision": obj.get("currentRevision"),
            "transactionSetIdentifierCode": obj.get("transactionSetIdentifierCode"),
            "transactionControlNumber": obj.get("transactionControlNumber"),
            "functionalIdentifierCode": obj.get("functionalIdentifierCode"),
            "functionalGroupControlNumber": obj.get("functionalGroupControlNumber"),
            "x12Version": obj.get("x12Version"),
            "stage": obj.get("stage"),
            "status": obj.get("status"),
            "code": obj.get("code"),
            "safeMessage": obj.get("safeMessage"),
            "line": obj.get("line"),
            "column": obj.get("column"),
            "fallback": obj.get("fallback"),
            "timestamp": obj.get("timestamp"),
            "replayId": obj.get("replayId"),
            "replayOfAttemptId": obj.get("replayOfAttemptId"),
            "resolved": obj.get("resolved"),
            "resolvedAt": obj.get("resolvedAt"),
            "resolvedByAttemptId": obj.get("resolvedByAttemptId")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
