#!/usr/bin/env python3
"""This module contains a function that takes a string and a
number (int or float) and returns a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing a string and a int or float."""
    return (k, v ** 2)
