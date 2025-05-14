#!/usr/bin/env python3
"""Defines a class FIFOCache that inherits from BaseCaching and is
    is a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache defines a FIFO caching system"""

    def __init__(self):
        """Initialize the FIFO cache"""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item with key"""
        return self.cache_date.get(key, None)
