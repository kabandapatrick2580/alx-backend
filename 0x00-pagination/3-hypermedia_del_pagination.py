#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Optional


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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None, page_size:
                        int = 10) -> Dict:
        """
        Get a hypermedia representation of a dataset page based on index.

        Args:
            index (Optional[int]): The start index of the return page.
                                    Default is None.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            Dict: A dictionary containing hypermedia representation of the
                    dataset page.
        """
        the_dataset_length = len(self.dataset())
        if index is None:
            index = 0
        else:
            assert 0 <= index < the_dataset_length, "Index out of range"

        next_index = min(index + page_size, the_dataset_length)
        data = [self.indexed_dataset().get(i) for i in range(
            index, next_index)
                ]

        the_hyper_data = {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }

        return the_hyper_data
