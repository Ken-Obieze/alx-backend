#!/usr/bin/env python3
"""FIFOCache module."""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class inherits from BaseCaching"""

    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.lru_list.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.lru_list.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.lru_list.remove(key)
        self.lru_list.append(key)

        return self.cache_data[key]
