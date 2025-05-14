#!/usr/bin/env python3
""" LFU caching module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines a LFU caching system with LRU tie-breaker
    """

    def __init__(self):
        """ Initialize the LFU cache
        """
        super().__init__()
        self.freq = defaultdict(OrderedDict)
        self.key_freq = {}
        self.min_freq = 1

    def __update_freq(self, key):
        """ Update frequency of a key and maintain the frequency structure
        Args:
            key: Key to update frequency for
        """
        curr_freq = self.key_freq[key]
        self.freq[curr_freq].pop(key)
        if not self.freq[curr_freq] and curr_freq == self.min_freq:
            self.min_freq += 1

        new_freq = curr_freq + 1
        self.key_freq[key] = new_freq
        self.freq[new_freq][key] = None

    def put(self, key, item):
        """ Add an item in the cache using LFU policy with LRU tie-breaker
        Args:
            key: Key to identify the item
            item: Value to be stored
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.__update_freq(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the LFU key(s)
            lfu_keys = self.freq[self.min_freq]
            # Use LRU to break ties (first item is least recently used)
            discard_key, _ = lfu_keys.popitem(last=False)
            del self.cache_data[discard_key]
            del self.key_freq[discard_key]
            print(f"DISCARD: {discard_key}")

        # Add new item
        self.cache_data[key] = item
        self.key_freq[key] = 1
        self.freq[1][key] = None
        self.min_freq = 1

    def get(self, key):
        """ Get an item by key
        Args:
            key: Key to look up in cache
        Returns:
            The value associated with the key or None if key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None

        self.__update_freq(key)
        return self.cache_data[key]
