#!/usr/bin/env python3
""" returning sum of input floats """
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    sum_list float.

    Args:
        input_list (list[float]): list of floats

    Returns:
        float: sum of input list.
    """
    return sum(input_list)
