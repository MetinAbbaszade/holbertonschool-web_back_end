#!/usr/bin/env python3
""" returns a function that multiplies a float """
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Returns a function that multiplies a float by a multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that multiplies a float.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
