#!/usr/bin/env python3
""" FIFO cache implementation"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """First in first out system of cache
    if the cache is fulk the first item
    into the cache is removed"""
    def __init__(self):
        """ Initialization"""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Assigns an item to its key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            old_key = self.keys_order.pop(-1)
            del self.cache_data[old_key]
            print(f'DISCARD: {old_key}')
        self.keys_order.append(key)

    def get(self, key):
        """Returns the values assocoated eoth the key"""
        return self.cache_data.get(key)
