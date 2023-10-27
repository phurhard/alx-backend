#!/usr/bin/env python3
""" Pagination implementation"""
import csv
import math
import typing
from typing import List, Dict


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
                dataset = list(reader)
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ This methods gets the required page contents"""
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        self.dataset()
        total_pages = (len(self.__dataset) + page_size) // page_size
        if not 1 <= page <= total_pages:
            return []
        start_index = (page_size * page) - page_size
        return self.__dataset[start_index:page_size * page]

    def get_hyper(self, page: int = 1, page_size: int =
                  10) -> Dict[str, typing.Union[str, int]]:
        """returns same as get_page but this time it's hyper sensitive"""
        self.dataset()
        total_pages = (len(self.__dataset) + page_size - 1) // page_size
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page != 1 else None
        data = self.get_page(page, page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
