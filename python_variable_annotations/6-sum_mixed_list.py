#!/usr/bin/env python3
""" returning sum of float and integers """
import typing


def sum_mixed_list(mxd_lst: typing.Union[int, float]) -> float:
    """
    sum_mixed_list float.

    Args:
        mxd_lst (Union[int, float]): list of floats and integers

    Returns:
        float: sum of input list.
    """
    return sum(mxd_lst)
