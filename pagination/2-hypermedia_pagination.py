#!/usr/bin/env python3
"""Simple pagination implementation."""

import csv
import math
from typing import List, Dict

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
        """Get a page of data from the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            List[List]: A list of lists representing the page of data.
        """
        assert (
            isinstance(page, int) and page > 0
        )
        assert (
            isinstance(page_size, int) and page_size > 0
        )

        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.dataset()):
            return []

        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get hypermedia pagination information.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            Dict: A dictionary containing pagination information and data.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        hypermedia_info = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hypermedia_info
    

if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))