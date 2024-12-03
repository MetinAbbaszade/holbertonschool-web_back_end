#!/usr/bin/env python3
""" advance task """
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
                        typing.Optional[typing.Any]:
    """
    Returns the first element of a list if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): The list to be evaluated.

    Returns:
        Union[Any, None]: The first element of the list if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
