#!/usr/bin/env python3
"""This module contains a function that sums a list of mixed
integers and floats with type annotations."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of mixed integers and floats."""
    return sum(mxd_lst)
