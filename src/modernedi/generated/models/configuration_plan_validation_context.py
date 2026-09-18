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

class ConfigurationPlanValidationContext(BaseModel):
    """
    Immutable syntax-tree catalog identity used while validating desired mappings. Both fields are null when no active catalog identity is available.
    """ # noqa: E501
    syntax_tree_catalog_revision: Optional[StrictStr] = Field(description="Active immutable syntax-tree catalog revision used by mapping validation.", alias="syntaxTreeCatalogRevision")
    syntax_tree_catalog_manifest_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(description="Lowercase SHA-256 of the active syntax-tree catalog manifest.", alias="syntaxTreeCatalogManifestSha256")
    scenario_authority_etag: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Present when scenario bindings are planned. Fences the current definitions, adapters, syntax trees, partners and mappings used for validation; apply rechecks this authority.", alias="scenarioAuthorityEtag")
    __properties: ClassVar[List[str]] = ["syntaxTreeCatalogRevision", "syntaxTreeCatalogManifestSha256", "scenarioAuthorityEtag"]

    @field_validator('syntax_tree_catalog_manifest_sha256', mode="before")
    def syntax_tree_catalog_manifest_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('scenario_authority_etag', mode="before")
    def scenario_authority_etag_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of ConfigurationPlanValidationContext from a JSON string"""
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
        # set to None if syntax_tree_catalog_revision (nullable) is None
        # and model_fields_set contains the field
        if self.syntax_tree_catalog_revision is None and "syntax_tree_catalog_revision" in self.model_fields_set:
            _dict['syntaxTreeCatalogRevision'] = None

        # set to None if syntax_tree_catalog_manifest_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.syntax_tree_catalog_manifest_sha256 is None and "syntax_tree_catalog_manifest_sha256" in self.model_fields_set:
            _dict['syntaxTreeCatalogManifestSha256'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationPlanValidationContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "syntaxTreeCatalogRevision": obj.get("syntaxTreeCatalogRevision"),
            "syntaxTreeCatalogManifestSha256": obj.get("syntaxTreeCatalogManifestSha256"),
            "scenarioAuthorityEtag": obj.get("scenarioAuthorityEtag")
        }.items() if key in obj})
        return _obj
