#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # LIFO: remove the last item added
                key_discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[ key_discarded_key]
                print("DISCARD:",  key_discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None
