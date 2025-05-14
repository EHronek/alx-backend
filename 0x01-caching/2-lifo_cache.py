#!/usr/bin/env python3
"""Defines a class LIFOCache that inherits from BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Last-in First-out cache system"""
    def __init__(self):
        """Initializes the LIFOCache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Adds an item in the LIFO Cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.stack.pop()
                del self.cache_data[discarded]
                print("DISCARD:", discarded)
            self.stack.append(key)
        else:
            self.stack.remove(key)
            self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key"""
        return self.cache_data.get(key, None)
