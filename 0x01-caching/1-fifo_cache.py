#!/usr/bin/env python3
"""FIFOCache module."""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class inherits from BaseCaching and represents a caching system """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            del self.cache_data[first_item]
            print("DISCARD: {}".format(first_item))

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
