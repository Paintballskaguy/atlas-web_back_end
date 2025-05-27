#!/usr/bin/env python3

"""
A caching system that implements the LRU (Least Recently Used) eviction policy.
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A caching system that implements the LRU (Least Recently Used) eviction policy.
    """
    def __init__(self):
        """Initialize the LIFO cach and track insert order"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """add an item to the cache following the LRU policy"""
        if key is not None and item is not None:
            # Updates existing key position in the stack
            if key in self.cache_data:
                self.usage_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # takes out last item added
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.usage.append(key)

    def get(self, key):
        """retrieve item from the cache by key id# and update its usage"""
        if key is not None and key in self.cache_data:
            # Update the usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
