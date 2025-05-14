#!/usr/bin/env python3
""" MRU caching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a MRU caching system
    """

    def __init__(self):
        """ Initialize the MRU cache
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache using MRU policy
        Args:
            key: Key to identify the item
            item: Value to be stored
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.usage_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        Args:
            key: Key to look up in cache
        Returns:
            The value associated with the key or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None

        # Update usage order (move to end as most recently used)
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
