#!/usr/bin/env python3
"""Module to Implement a get_hyper method."""
import csv
import math
from typing import List, Dict, Union, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the corresponding page of the dataset for the given page
        """
        assert isinstance(page, int) and \
                page > 0, "page must be an integer greater than 0"
        assert isinstance(page_size, int) and \
                page_size > 0, "page_size must be an integer greater than 0"

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary containing the pagination information
        """
        assert isinstance(page, int) and \
                page > 0, "page must be an integer greater than 0"
        assert isinstance(page_size, int) and \
                page_size > 0, "page_size must be an integer greater than 0"

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return {
                "page_size": 0,
                "page": page,
                "data": [],
                "next_page": None,
                "prev_page": None,
                "total_pages": total_pages
            }

        data = dataset[start:end]
        next_page = page + 1 if end < len(dataset) else None
        prev_page = page - 1 if start > 0 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return tuple containing a start index and an end index.

    Args:
        page (int): The 1-indexed page number.
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: The start index and end index of the page range.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
