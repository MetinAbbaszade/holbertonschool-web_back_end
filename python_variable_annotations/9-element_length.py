#!/usr/bin/env python3
import typing
""" returning tuple but in list:d"""


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
                        typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Returns a list of the lengths of the elements in a list of strings.

    Args:
        lst (List[str]): The list of strings to be measured.

    Returns:
        List[int]: The list of lengths of the elements in the list of strings.
    """
    return [(i, len(i)) for i in lst]
