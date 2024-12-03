#!/usr/bin/env python3
""" file for returning tuple """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    to_kv Tuple.

    Args:
        k (str): string
        v (int or float): number

    Returns:
        string and square of int or float
    """
    return (k, v**2)
