# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappedOutputWebhookUpdateRequest(BaseModel):
    """
    MappedOutputWebhookUpdateRequest
    """ # noqa: E501
    enabled: StrictBool = Field(description="Enables or disables push delivery for this partner. Disabling retains the stored endpoint and signing secret for later use; re-enabling still requires `endpointUrl` in this request.")
    endpoint_url: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(default=None, description="Required when `enabled` is true. Must be an absolute HTTPS URL without user information or a fragment and use a publicly routable host. DNS is revalidated before every delivery.", alias="endpointUrl", json_schema_extra={"examples": ["https://erp.example.com/webhooks/modernedi"]})
    rotate_signing_secret: Optional[StrictBool] = Field(default=False, description="When true on an enabled webhook, replaces the signing secret and returns the new plaintext value once. Enabling a webhook without an existing secret creates one even when this is false.", alias="rotateSigningSecret")
    __properties: ClassVar[List[str]] = ["enabled", "endpointUrl", "rotateSigningSecret"]

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
        """Create an instance of MappedOutputWebhookUpdateRequest from a JSON string"""
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
        # set to None if endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_url is None and "endpoint_url" in self.model_fields_set:
            _dict['endpointUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappedOutputWebhookUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "enabled": obj.get("enabled"),
            "endpointUrl": obj.get("endpointUrl"),
            "rotateSigningSecret": obj.get("rotateSigningSecret") if obj.get("rotateSigningSecret") is not None else False
        }.items() if key in obj})
        return _obj
