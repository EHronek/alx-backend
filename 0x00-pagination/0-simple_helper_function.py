#!/usr/bin/env python3
"""Defines a function that takes two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing a start index and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
