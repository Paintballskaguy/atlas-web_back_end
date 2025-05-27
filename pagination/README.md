# Pagination Projects

A collection of Python implementations for different pagination strategies.

## Tasks

### 0. Simple Helper Function
**File:** `0-simple_helper_function.py`  
Implement `index_range(page: int, page_size: int) -> tuple` that calculates start and end indexes for pagination.

### 1. Simple Pagination
**File:** `1-simple_pagination.py`  
Implement `Server.get_page()` that:
- Uses `index_range` to paginate dataset
- Returns the correct page of data
- Handles out-of-range requests

### 2. Hypermedia Pagination
**File:** `2-hypermedia_pagination.py`  
Implement `Server.get_hyper()` that extends basic pagination to include:
- Current page size
- Next/previous page numbers
- Total page count
- Page data

### 3. Deletion-Resilient Hypermedia Pagination
**File:** `3-hypermedia_del_pagination.py`  
Implement `Server.get_hyper_index()` that:
- Uses indexed dataset to handle deletions
- Maintains consistency when items are removed
- Returns hypermedia format with:
  - Current index
  - Next index
  - Page data
  - Page size

## Requirements
- Python 3.9
- Ubuntu 20.04 LTS
- pycodestyle (2.5.*)
- All files must end with newline
- Type annotations for all functions
- Proper documentation for modules and functions

## Usage
```python
from 1-simple_pagination import Server
server = Server()
print(server.get_page(1, 3))