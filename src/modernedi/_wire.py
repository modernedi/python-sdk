"""Serialize nested union values using their wire representation, not Pydantic internals."""
from uuid import UUID


def to_wire_value(value):
    if hasattr(value, "to_dict"):
        return to_wire_value(value.to_dict())
    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, (list, tuple)):
        return [to_wire_value(item) for item in value]
    if isinstance(value, dict):
        return {key: to_wire_value(item) for key, item in value.items()}
    return value
