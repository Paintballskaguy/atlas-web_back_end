#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[
        str, Optional[Union[int, List[List]]]]:
        """Get deletion-resilient hypermedia pagination info.

        Args:
            index: Current start index (None defaults to 0)
            page_size: Number of items per page

        Returns:
            Dictionary containing:
                - index: current start index
                - data: page of dataset
                - page_size: current page size
                - next_index: next index to query
        """
        assert index is None or (isinstance(index, int) and index >= 0), (
            "index must be non-negative integer or None"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be positive integer"
        )

        indexed_data = self.indexed_dataset()
        max_index = max(indexed_data.keys()) if indexed_data else 0

        # Handle None index case
        if index is None:
            index = 0

        # Find the next available index if current is deleted
        while index not in indexed_data and index <= max_index:
            index += 1

        # Collect data for the current page
        data = []
        current_index = index
        items_collected = 0

        while items_collected < page_size and current_index <= max_index:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                items_collected += 1
            current_index += 1

        # Determine next index
        next_index = current_index if current_index <= max_index else None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
