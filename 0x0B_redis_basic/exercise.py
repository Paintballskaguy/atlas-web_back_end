#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times any method is called"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store history of inputs and outputs"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        input_args = args[1:]
        input_str = str(input_args)
        self._redis.rpush(inputs_key, input_str)

        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)

        return output
    return wrapper


class Cache:
    def __init__(self):
        """start the Redis client and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:

        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieves data and converts it to a UTF-8 str"""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Retrieve data and converts it to a int"""
        return self.get(key, fn=int)

    def replay(method: Callable) -> None:
        """Display the history of calls of a particular function"""
        cache_instance = method.__self__
        qualname = method.__qualname__

        inputs = cache_instance._redis.lrange(f"{qualname}:inputs", 0, -1)
        outputs = cache_instance._redis.lrange(f"{qualname}:outputs", 0, -1)

        inputs = [inp.decode('utf-8') for inp in inputs]
        outputs = [out.decode('utf-8') for out in outputs]

        print(f"{qualname} was called {len(inputs)} times:")
        for args, output in zip(inputs, outputs):
            print(f"{qualname}(*{args}) -> {output}")
