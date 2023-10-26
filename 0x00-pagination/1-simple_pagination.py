#!/usr/bin/env python3
"""Module to Implement a method named get_page."""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """
        Return list of rows from dataset corresponding to page and size.

        Args:
            page (int, optional): The 1-indexed page number. Defaults to 1.
            page_size (int, optional): number of items. Defaults to 10.

        Returns:
            List[List]: The list of rows corresponding to the page and size.
        """
        assert isinstance(page, int) and \
                page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and \
                page_size > 0, "page_size must be a positive integer"
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(dataset):
            return []
        return dataset[start:end]
