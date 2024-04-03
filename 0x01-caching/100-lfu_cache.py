#!/usr/bin/python3
""" LFUCache module.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = {}
        self.key_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key exists, move it to the end of key_order
                self.key_order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Find least frequency used item(s)
                min_freq = min(self.frequency.values())
                key_lfu_keys = [
                            k for k, v in self.frequency.items()
                            if v == min_freq
                            ]

                # If more than one least frequency used item, use LRU to decide
                if len(key_lfu_keys) > 1:
                    lru_key = self.key_order.pop(0)
                    key_lfu_keys.remove(lru_key)
                    del self.cache_data[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    key_lfu_key = key_lfu_keys[0]
                    del self.cache_data[key_lfu_key]
                    print("DISCARD:", key_lfu_key)

                del self.frequency[key_lfu_key]

            self.key_order.append(key)
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            # Update frequency
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
