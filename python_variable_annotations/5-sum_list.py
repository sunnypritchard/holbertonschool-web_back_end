#!/usr/bin/env python3
"""This module contains a function that sums a list of float numbers."""


def sum_list(input_list: list[float]) -> float:
    """Returns the sum of a list of float numbers."""
    total: float = 0.0
    for num in input_list:
        total += num
    return total
