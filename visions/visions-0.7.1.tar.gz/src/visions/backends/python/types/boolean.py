from typing import Sequence

from visions.backends.python.series_utils import (
    sequence_handle_none,
    sequence_not_empty,
)
from visions.types import Boolean, Object, String


@sequence_not_empty
@sequence_handle_none
def is_bool(sequence: Sequence, state: dict):
    return all(isinstance(value, bool) for value in sequence)


def to_bool(sequence: Sequence, state: dict):
    return map(bool, sequence)


@Boolean.register_relationship(Object, Sequence)
def object_is_bool(sequence: Sequence, state: dict) -> bool:
    return is_bool(sequence, state)


@Boolean.register_transformer(Object, Sequence)
def object_to_bool(sequence: Sequence, state: dict) -> Sequence:
    return to_bool(sequence, state)


@Boolean.register_relationship(String, Sequence)
@sequence_handle_none
def string_is_bool(sequence: Sequence, state: dict):
    return all(value.lower() in {"true", "false"} for value in sequence)


@Boolean.register_transformer(String, Sequence)
def string_to_bool(sequence: Sequence, state: dict):
    return map(lambda v: v.lower() == "true" if isinstance(v, str) else v, sequence)


@Boolean.contains_op.register
def boolean_contains(sequence: Sequence, state: dict) -> bool:
    return is_bool(sequence, state)
