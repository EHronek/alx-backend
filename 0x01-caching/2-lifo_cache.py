#!/usr/bin/env python3
"""Defines a class LIFOCache that inherits from BaseCaching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last-in First-out cache system"""
    def __init(self):
        """Initializes the LIFOCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the LIFO Cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1
