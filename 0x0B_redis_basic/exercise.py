#!/usr/bin/env python3


import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """start the Redis client and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Storing the input data in Redis with a random key

        Args:
            data (Union[str, bytes, int, float]): Data to be stored,
            can be str, bytes, int, or float.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
