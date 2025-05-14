#!/usr/bin/env python3
"""LRU caching module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache defines LRU caching system"""
    def __init__(self):
        """Initialize the LRU cache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item in the cache using LRU policy"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.usage_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
