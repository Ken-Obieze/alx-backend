#!/usr/bin/env python3
"""Module for index_range."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return tuple of size two containing a start index and end index.

    corresponding to the range of indexes to return in a list for the given.

    pagination parameters.

    Args:
        page (int): The 1-indexed page number.
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: The start index and end index of the page range.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
