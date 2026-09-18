"""Serialize nested union values using their wire representation, not Pydantic internals."""
def to_wire_value(value):
    if hasattr(value, "to_dict"):
        return to_wire_value(value.to_dict())
    if isinstance(value, list):
        return [to_wire_value(item) for item in value]
    if isinstance(value, dict):
        return {key: to_wire_value(item) for key, item in value.items()}
    return value
