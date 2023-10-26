#!/usr/bin/env python3
"""FIFOCache module."""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class inherits from BaseCaching"""

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq_keys = self.frequency[self.min_frequency]
            lfu_key = min_freq_keys.pop(0)
            del self.cache_data[lfu_key]
            print("DISCARD: {}".format(lfu_key))

            if not min_freq_keys:
                del self.frequency[self.min_frequency]

        self.cache_data[key] = item
        self.frequency.setdefault(1, []).append(key)
        self.min_frequency = 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        freq = self.get_frequency(key)
        self.frequency[freq].remove(key)
        if not self.frequency[freq]:
            del self.frequency[freq]

        freq += 1
        self.frequency.setdefault(freq, []).append(key)
        self.update_min_frequency(freq)

        return self.cache_data[key]

    def get_frequency(self, key):
        """ Get the frequency of a key """
        for freq, keys in self.frequency.items():
            if key in keys:
                return freq
        return 0

    def update_min_frequency(self, freq):
        """ Update the minimum frequency """
        if freq < self.min_frequency or self.min_frequency not in self.frequency:
            self.min_frequency = freq
