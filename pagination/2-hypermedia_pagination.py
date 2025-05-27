#!/usr/bin/env python3

"""
Module that helps with pagination calculations.
"""


import csv
import math
from typing import List, Dict, Optional, Union


def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end index of pagination

    Args:
        page (int): The current page number (1-indexed)
        page_size (int): The number of items per page

    Returns:
        tuple: A tuple containing the start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        """Retrieve a page of data from the dataset.

        Args:
            page (int, optional): The page number (1-indexed)
            page_size (int, optional): The number of items per page

        Returns:
            List[List]:
            The requested page of data or empty list if out of range.
        """
        assert isinstance(page, int) and page > 0, (
            "page must be a positive integer")
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be a positive integer")

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        return dataset[start:end] if start < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[
            str, Optional[Union[int, List[List]]]]:
        """Returns hypermedia pagination information for the dataset.

        Args:
            page: Current page number (1-indexed)
            page_size: Number of items per page

        Returns:
            Dictionary containing:
                - page_size: Number of items in current page
                - page: Current page number
                - data: List of items on current page
                - next_page: Next page number or None
                - prev_page: Previous page number or None
                - total_pages: Total number of pages
        """
        page_data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size) if page_size > 0 else 0

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
