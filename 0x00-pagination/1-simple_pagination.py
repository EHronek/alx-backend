#!/usr/bin/env python3
"""simple pagination"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        start, end = index_range(page, page_size)

        data = self.dataset()

        return data[start:end]
