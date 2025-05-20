#!/usr/bin/env python3

"""caching system that implements the LIFO
(Last-in-First-Out) eviction policy
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that implements a Last-In-First-Out caching system.
    """
    def __init__(self):
        """Initialize the LIFO cach and track insert order"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """add an item to the cache following the LIFO policy"""
        if key is not None and item is not None:
            # Updates existing key position in the stack
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # takes out last item added
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """retrieve item from the cache by key id#"""
        if key is not None:
            return self.cache_data.get(key, None)
        return None
