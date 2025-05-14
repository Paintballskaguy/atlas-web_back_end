# Async Comprehension and Runtime Measurement

This project demonstrates asynchronous programming in Python using async comprehensions and parallel execution.

## Files

1. `0-async_generator.py`  
   - Coroutine `async_generator` that yields 10 random numbers (0-10) with 1-second delays

2. `1-async_comprehension.py`  
   - Coroutine `async_comprehension` that collects 10 random numbers using async comprehension

3. `2-measure_runtime.py`  
   - Coroutine `measure_runtime` that executes 4 parallel comprehensions and measures total time

## Requirements

- Python 3.9
- Ubuntu 20.04 LTS
- pycodestyle (2.5.x)

## Key Concepts

- Async/await syntax
- Async generators
- Async comprehensions
- Parallel execution with `asyncio.gather`
- Runtime measurement

## Expected Output

Running `2-main.py` will output approximately 10 seconds, demonstrating that:
- Each comprehension takes ~10 seconds
- 4 run in parallel take ~10 seconds total (not 40)
- Sleep operations overlap during async execution

## Style

All code follows pycodestyle guidelines with:
- Type annotations
- Complete documentation
- 79-character line limits
- Proper whitespace usage