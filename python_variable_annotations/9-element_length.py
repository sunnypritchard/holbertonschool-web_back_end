#!/usr/bin/env python3
"""This module contains a function that takes a list of tuples
and returns a list of their lengths with type annotations."""

from typing import List, Tuple


def element_length(lst: List[Tuple]) -> List[int]:
    """Returns a list of lengths of the tuples in the input list."""
    return [len(i) for i in lst]
