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
from modernedi.generated.models.usage_day import UsageDay
from modernedi.generated.models.usage_hour import UsageHour
from modernedi.generated.models.usage_partner_breakdown import UsagePartnerBreakdown
from modernedi.generated.models.usage_signals import UsageSignals
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UsageSnapshot(BaseModel):
    """
    Workspace AS2-message usage and self-service plan enforcement state, measured in UTC.
    """ # noqa: E501
    as_of: str = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`.", alias="asOf", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    time_zone: StrictStr = Field(description="Time zone defining daily and hourly buckets; currently always `UTC`.", alias="timeZone", json_schema_extra={"examples": ["UTC"]})
    plan_code: Optional[StrictStr] = Field(default=None, description="Current billing plan code, or `null` when billing metadata is unavailable.", alias="planCode")
    daily_limit: Optional[StrictInt] = Field(default=None, description="Included AS2 messages per UTC day, or `null` for an unlimited plan.", alias="dailyLimit")
    warning_threshold: Optional[StrictInt] = Field(default=None, description="Attempted-message count that changes `status` to `approaching_limit`, or `null` for unlimited plans.", alias="warningThreshold")
    rejection_threshold: Optional[StrictInt] = Field(default=None, description="Attempted-message count after which new AS2 messages are rejected, or `null` for unlimited plans.", alias="rejectionThreshold")
    attempted_messages_today: StrictInt = Field(description="AS2 messages attempted since 00:00 UTC, including accepted and rejected messages.", alias="attemptedMessagesToday")
    accepted_messages_today: StrictInt = Field(description="AS2 messages accepted for processing since 00:00 UTC.", alias="acceptedMessagesToday")
    rejected_messages_today: StrictInt = Field(description="AS2 messages rejected by quota enforcement since 00:00 UTC.", alias="rejectedMessagesToday")
    quarantine_retention_days: Optional[StrictInt] = Field(default=None, description="Days quota-rejected payloads are retained for support recovery, or `null` when enforcement is not configured.", alias="quarantineRetentionDays")
    rejection_active: StrictBool = Field(description="True when attempted usage has crossed the rejection threshold and new messages are being rejected.", alias="rejectionActive")
    unlimited: StrictBool = Field(description="True when this workspace has no configured daily AS2 message limit.")
    status: StrictStr = Field(description="Stable state: `ok`, `approaching_limit`, `over_limit`, `rejection_active`, or `unlimited`.")
    enforcement_mode: StrictStr = Field(description="Machine-readable quota behavior, currently `reject_after_safety_threshold` or `not_configured`.", alias="enforcementMode")
    policy: StrictStr = Field(description="Customer-readable explanation of the workspace's current quota and safety-threshold policy.")
    today: UsageDay
    daily_usage: List[UsageDay] = Field(description="Daily accepted-message totals for the retained usage window, ordered by date.", alias="dailyUsage")
    today_by_partner: List[UsagePartnerBreakdown] = Field(description="Current UTC-day accepted messages and transaction rows grouped by partner.", alias="todayByPartner")
    today_by_hour: List[UsageHour] = Field(description="Current UTC-day accepted messages and transaction rows grouped into UTC hour buckets.", alias="todayByHour")
    signals: UsageSignals
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["asOf", "timeZone", "planCode", "dailyLimit", "warningThreshold", "rejectionThreshold", "attemptedMessagesToday", "acceptedMessagesToday", "rejectedMessagesToday", "quarantineRetentionDays", "rejectionActive", "unlimited", "status", "enforcementMode", "policy", "today", "dailyUsage", "todayByPartner", "todayByHour", "signals"]

    @field_validator('as_of', mode="before")
    def as_of_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
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
        """Create an instance of UsageSnapshot from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of today
        if self.today:
            _dict['today'] = self.today.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in daily_usage (list)
        _items = []
        if self.daily_usage:
            for _item_daily_usage in self.daily_usage:
                if _item_daily_usage:
                    _items.append(_item_daily_usage.to_dict())
            _dict['dailyUsage'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in today_by_partner (list)
        _items = []
        if self.today_by_partner:
            for _item_today_by_partner in self.today_by_partner:
                if _item_today_by_partner:
                    _items.append(_item_today_by_partner.to_dict())
            _dict['todayByPartner'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in today_by_hour (list)
        _items = []
        if self.today_by_hour:
            for _item_today_by_hour in self.today_by_hour:
                if _item_today_by_hour:
                    _items.append(_item_today_by_hour.to_dict())
            _dict['todayByHour'] = _items
        # override the default output from pydantic by calling `to_dict()` of signals
        if self.signals:
            _dict['signals'] = self.signals.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if plan_code (nullable) is None
        # and model_fields_set contains the field
        if self.plan_code is None and "plan_code" in self.model_fields_set:
            _dict['planCode'] = None

        # set to None if daily_limit (nullable) is None
        # and model_fields_set contains the field
        if self.daily_limit is None and "daily_limit" in self.model_fields_set:
            _dict['dailyLimit'] = None

        # set to None if warning_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.warning_threshold is None and "warning_threshold" in self.model_fields_set:
            _dict['warningThreshold'] = None

        # set to None if rejection_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.rejection_threshold is None and "rejection_threshold" in self.model_fields_set:
            _dict['rejectionThreshold'] = None

        # set to None if quarantine_retention_days (nullable) is None
        # and model_fields_set contains the field
        if self.quarantine_retention_days is None and "quarantine_retention_days" in self.model_fields_set:
            _dict['quarantineRetentionDays'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsageSnapshot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "asOf": obj.get("asOf"),
            "timeZone": obj.get("timeZone"),
            "planCode": obj.get("planCode"),
            "dailyLimit": obj.get("dailyLimit"),
            "warningThreshold": obj.get("warningThreshold"),
            "rejectionThreshold": obj.get("rejectionThreshold"),
            "attemptedMessagesToday": obj.get("attemptedMessagesToday"),
            "acceptedMessagesToday": obj.get("acceptedMessagesToday"),
            "rejectedMessagesToday": obj.get("rejectedMessagesToday"),
            "quarantineRetentionDays": obj.get("quarantineRetentionDays"),
            "rejectionActive": obj.get("rejectionActive"),
            "unlimited": obj.get("unlimited"),
            "status": obj.get("status"),
            "enforcementMode": obj.get("enforcementMode"),
            "policy": obj.get("policy"),
            "today": UsageDay.from_dict(obj["today"]) if obj.get("today") is not None else None,
            "dailyUsage": [UsageDay.from_dict(_item) for _item in obj["dailyUsage"]] if obj.get("dailyUsage") is not None else None,
            "todayByPartner": [UsagePartnerBreakdown.from_dict(_item) for _item in obj["todayByPartner"]] if obj.get("todayByPartner") is not None else None,
            "todayByHour": [UsageHour.from_dict(_item) for _item in obj["todayByHour"]] if obj.get("todayByHour") is not None else None,
            "signals": UsageSignals.from_dict(obj["signals"]) if obj.get("signals") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
