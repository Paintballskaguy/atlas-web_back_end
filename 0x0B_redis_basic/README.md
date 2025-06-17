# Redis-based Cache System
- This project implements a Redis-based caching system with method call tracking and history replay capabilities. It uses decorators to count method calls and store input/output history in Redis, providing a powerful way to monitor and analyze cache operations.

## Features
Redis-backed caching: Store strings, bytes, integers, and floats with automatic key generation

Method call tracking: Decorators to count how many times methods are called

Call history: Store input parameters and outputs for each method call

History replay: Display complete call history with inputs and outputs

Type conversion: Retrieve cached values as strings or integers