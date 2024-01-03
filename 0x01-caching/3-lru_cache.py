#!/usr/bin/env python
"""Least Recently Used Recency Based Policy """


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implementation of the LRUCache class"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put key/item in the cache while using the LRUCache
        if the cache gets filled up"""
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            pass

    def get(self, key):
        """Get the item in the cache with the provided key"""
        if key is None:
            return None
        return self.cache_data.get(key)