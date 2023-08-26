#!/usr/bin/env python3
"""caching is a process of
saving data on the RAM"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system"""
    def __init__(self):
        """Initializer"""
        super().__init__()

    def put(self, key, item):
        """Assigs the item to the key in the cache database"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value of the key"""
        return self.cache_data.get(key)
