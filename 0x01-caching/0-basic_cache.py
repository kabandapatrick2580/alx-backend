from base_caching import BaseCaching
class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key associated with the item.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache based on the provided key.

        Args:
            key: The key associated with the item to retrieve.

        Returns:
            The value associated with the provided key, or None if the key is None or not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or not found in cache_data
        return self.cache_data[key]
