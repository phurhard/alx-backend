#!/usr/bin/env python3
""" Pagination implementation"""
import csv
import math
from typing import List


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
        """ This methods gets the required page contents"""
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        self.dataset()
        total_pages = (len(self.__dataset) + page_size) // page_size
        if 1 <= page <= total_pages:

            start_index = (page_size * page) - page_size
            end_index = page_size * page
            req_page = self.__dataset[start_index:end_index]
            return req_page
        else:
            return []
