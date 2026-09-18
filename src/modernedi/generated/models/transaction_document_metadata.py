# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from modernedi._wire import to_wire_value
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from modernedi.generated.models.transaction_functional_acknowledgment_document import TransactionFunctionalAcknowledgmentDocument
from modernedi.generated.models.transaction_http_response_document import TransactionHttpResponseDocument
from modernedi.generated.models.transaction_implementation_acknowledgment_document import TransactionImplementationAcknowledgmentDocument
from modernedi.generated.models.transaction_mapped_output_document import TransactionMappedOutputDocument
from modernedi.generated.models.transaction_mdn_document import TransactionMdnDocument
from modernedi.generated.models.transaction_technical_acknowledgment_document import TransactionTechnicalAcknowledgmentDocument
from modernedi.generated.models.transaction_x12_document import TransactionX12Document
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

TRANSACTIONDOCUMENTMETADATA_ONE_OF_SCHEMAS = ["TransactionFunctionalAcknowledgmentDocument", "TransactionHttpResponseDocument", "TransactionImplementationAcknowledgmentDocument", "TransactionMappedOutputDocument", "TransactionMdnDocument", "TransactionTechnicalAcknowledgmentDocument", "TransactionX12Document"]

class TransactionDocumentMetadata(BaseModel):
    """
    Metadata for one retained transaction artifact. `type` selects the renderer and concrete `metadata` schema. The MDN shapes are further distinguished by stable `id`: `mdn-report` contains receipt-assurance metadata, while `functional-ack-mdn-report` and `implementation-ack-mdn-report` contain the Message-Id and disposition of the 997's or 999's own MDN. Document indexes never include `content`.
    """
    # data type: TransactionX12Document
    oneof_schema_1_validator: Optional[TransactionX12Document] = None
    # data type: TransactionMappedOutputDocument
    oneof_schema_2_validator: Optional[TransactionMappedOutputDocument] = None
    # data type: TransactionMdnDocument
    oneof_schema_3_validator: Optional[TransactionMdnDocument] = None
    # data type: TransactionFunctionalAcknowledgmentDocument
    oneof_schema_4_validator: Optional[TransactionFunctionalAcknowledgmentDocument] = None
    # data type: TransactionImplementationAcknowledgmentDocument
    oneof_schema_5_validator: Optional[TransactionImplementationAcknowledgmentDocument] = None
    # data type: TransactionTechnicalAcknowledgmentDocument
    oneof_schema_6_validator: Optional[TransactionTechnicalAcknowledgmentDocument] = None
    # data type: TransactionHttpResponseDocument
    oneof_schema_7_validator: Optional[TransactionHttpResponseDocument] = None
    actual_instance: Optional[Union[TransactionFunctionalAcknowledgmentDocument, TransactionHttpResponseDocument, TransactionImplementationAcknowledgmentDocument, TransactionMappedOutputDocument, TransactionMdnDocument, TransactionTechnicalAcknowledgmentDocument, TransactionX12Document]] = None
    one_of_schemas: Set[str] = { "TransactionFunctionalAcknowledgmentDocument", "TransactionHttpResponseDocument", "TransactionImplementationAcknowledgmentDocument", "TransactionMappedOutputDocument", "TransactionMdnDocument", "TransactionTechnicalAcknowledgmentDocument", "TransactionX12Document" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )

    discriminator_value_class_map: Dict[str, str] = {
        'TransactionDocument': 'TransactionDocument'
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = TransactionDocumentMetadata.model_construct()
        error_messages = []
        match = 0
        # validate data type: TransactionX12Document
        if not isinstance(v, TransactionX12Document):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionX12Document`")
        else:
            match += 1
        # validate data type: TransactionMappedOutputDocument
        if not isinstance(v, TransactionMappedOutputDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionMappedOutputDocument`")
        else:
            match += 1
        # validate data type: TransactionMdnDocument
        if not isinstance(v, TransactionMdnDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionMdnDocument`")
        else:
            match += 1
        # validate data type: TransactionFunctionalAcknowledgmentDocument
        if not isinstance(v, TransactionFunctionalAcknowledgmentDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionFunctionalAcknowledgmentDocument`")
        else:
            match += 1
        # validate data type: TransactionImplementationAcknowledgmentDocument
        if not isinstance(v, TransactionImplementationAcknowledgmentDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionImplementationAcknowledgmentDocument`")
        else:
            match += 1
        # validate data type: TransactionTechnicalAcknowledgmentDocument
        if not isinstance(v, TransactionTechnicalAcknowledgmentDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionTechnicalAcknowledgmentDocument`")
        else:
            match += 1
        # validate data type: TransactionHttpResponseDocument
        if not isinstance(v, TransactionHttpResponseDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionHttpResponseDocument`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TransactionDocumentMetadata with oneOf schemas: TransactionFunctionalAcknowledgmentDocument, TransactionHttpResponseDocument, TransactionImplementationAcknowledgmentDocument, TransactionMappedOutputDocument, TransactionMdnDocument, TransactionTechnicalAcknowledgmentDocument, TransactionX12Document. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TransactionDocumentMetadata with oneOf schemas: TransactionFunctionalAcknowledgmentDocument, TransactionHttpResponseDocument, TransactionImplementationAcknowledgmentDocument, TransactionMappedOutputDocument, TransactionMdnDocument, TransactionTechnicalAcknowledgmentDocument, TransactionX12Document. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into TransactionX12Document
        try:
            instance.actual_instance = TransactionX12Document.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionMappedOutputDocument
        try:
            instance.actual_instance = TransactionMappedOutputDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionMdnDocument
        try:
            instance.actual_instance = TransactionMdnDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionFunctionalAcknowledgmentDocument
        try:
            instance.actual_instance = TransactionFunctionalAcknowledgmentDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionImplementationAcknowledgmentDocument
        try:
            instance.actual_instance = TransactionImplementationAcknowledgmentDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionTechnicalAcknowledgmentDocument
        try:
            instance.actual_instance = TransactionTechnicalAcknowledgmentDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionHttpResponseDocument
        try:
            instance.actual_instance = TransactionHttpResponseDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransactionDocumentMetadata with oneOf schemas: TransactionFunctionalAcknowledgmentDocument, TransactionHttpResponseDocument, TransactionImplementationAcknowledgmentDocument, TransactionMappedOutputDocument, TransactionMdnDocument, TransactionTechnicalAcknowledgmentDocument, TransactionX12Document. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TransactionDocumentMetadata with oneOf schemas: TransactionFunctionalAcknowledgmentDocument, TransactionHttpResponseDocument, TransactionImplementationAcknowledgmentDocument, TransactionMappedOutputDocument, TransactionMdnDocument, TransactionTechnicalAcknowledgmentDocument, TransactionX12Document. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(to_wire_value(self.actual_instance), ensure_ascii=False, allow_nan=False)

    def to_dict(self) -> Optional[Union[Dict[str, Any], TransactionFunctionalAcknowledgmentDocument, TransactionHttpResponseDocument, TransactionImplementationAcknowledgmentDocument, TransactionMappedOutputDocument, TransactionMdnDocument, TransactionTechnicalAcknowledgmentDocument, TransactionX12Document]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return to_wire_value(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
