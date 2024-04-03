#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key exists, move it to the end of key_order
                self.key_order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Evict most recently used item
                key_mru_key = self.key_order.pop()
                del self.cache_data[key_mru_key]
                print("DISCARD:", key_mru_key)
            self.key_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            # Move key to the end of key_order (most recently used)
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None
