#!/usr/bin/env python3
"""0-simple_heleper_function module."""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start and end index
                        for the specified page.
    """
    the_start_index: int = (page - 1) * page_size
    the_end_index: int = the_start_index + page_size - 1
    return the_start_index, the_end_index
