# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class TransactionAttentionReason(str, Enum):
    """
    Machine-readable reason that a transaction needs operator attention. `functional_ack_issue` means a 997 was received but was not cleanly accepted. `implementation_ack_issue` means a 999 was received but the transaction-specific IK5 result or conservative AK9 group result was not cleanly accepted. `x12_ack_overdue` means neither a 997 nor a 999 was received for an eligible outbound business transaction by `x12AcknowledgmentExpectedBy`; outbound 997 and 999 acknowledgment documents are excluded. The overdue signal does not automatically resend the original X12. `technical_ack_issue` means a requested TA1 was received but rejected the interchange, reported errors, or could not be classified. `technical_ack_overdue` means ISA14 requested a TA1 but none was received by `technicalAckExpectedBy`. Neither technical-acknowledgment reason automatically resends the original X12. `as2_mdn_attention` means the partner's AS2 receipt is overdue, rejected, invalid, contains a warning, or its returned content MIC does not match the content ModernEDI sent. ModernEDI never automatically resends a document in response to an MDN issue because the partner may already have processed it. `mapped_output_not_collected` means a managed output remained available beyond the 15-minute pickup grace period without a first delivery lease. `mapped_output_ack_overdue` means a delivered output was not acknowledged before its lease expired or was delivered more than once. One transaction can have more than one active reason.
    """

    """
    allowed enum values
    """
    MAPPING_FAILURE = 'mapping_failure'
    FUNCTIONAL_ACK_ISSUE = 'functional_ack_issue'
    IMPLEMENTATION_ACK_ISSUE = 'implementation_ack_issue'
    X12_ACK_OVERDUE = 'x12_ack_overdue'
    TECHNICAL_ACK_ISSUE = 'technical_ack_issue'
    TECHNICAL_ACK_OVERDUE = 'technical_ack_overdue'
    AS2_MDN_ATTENTION = 'as2_mdn_attention'
    MAPPED_OUTPUT_NOT_COLLECTED = 'mapped_output_not_collected'
    MAPPED_OUTPUT_ACK_OVERDUE = 'mapped_output_ack_overdue'
    WATCHLIST = 'watchlist'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionAttentionReason from a JSON string"""
        return cls(json.loads(json_str))
