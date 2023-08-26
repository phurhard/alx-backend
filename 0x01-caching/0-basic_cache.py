#!/usr/bin/env python3
""""caching"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system"""
    def __init__(self):
        """Initializer"""
        super()

    def put(self, key, item):
        """Assigs the item to the key in the cache database"""
        if key == None or item == None:
            return
        else:
            self.cached_data[key] = item

    def get(self, key):
        """Gets the value of the key"""
        return self.cached_data(key)