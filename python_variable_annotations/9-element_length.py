#!/usr/bin/env python3
"""This module contains a function that takes a list of sequences
and returns a list of tuples with each sequence and its length."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with each sequence and its length."""
    return [(i, len(i)) for i in lst]
