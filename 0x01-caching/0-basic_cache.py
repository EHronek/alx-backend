#!/usr/bin/env python3
"""Defines a class BasicCache that inherits from BaseCaching and is
a chaching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def __init__(self):
        """Initialization of the BasicCache"""
        super().__init__()

    def put(self, key, item):
        """assigns to the dictionary `self.cache_data` the item value"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
