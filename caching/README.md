# Caching Python Project

This project demonstrates various caching techniques in Python. It includes implementations of different cache types and usage examples.

## Features

- Multiple cache strategies (e.g., LRU, LFU, FIFO)
- Easy-to-use Python classes
- Example usage and test cases

## Getting Started

1. Clone the repository.
2. Install dependencies (if any).
3. Run the example scripts.

## Usage

```python
from cache import LRUCache

cache = LRUCache(capacity=3)
cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))  # Output: 1
```


