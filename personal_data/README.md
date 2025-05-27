# Secure Data Handling Module

This Python module provides tools for secure data handling including:
- PII (Personally Identifiable Information) redaction in logs
- Secure password hashing and validation
- Safe database connections

## Features

### 1. PII Redaction
- Filters sensitive fields from log messages
- Configurable list of PII fields to redact
- Uses regex pattern matching for efficient redaction

### 2. Password Security
- `hash_password(password: str) -> bytes`:
  - Securely hashes passwords using bcrypt with salt
  - Returns hashed password as bytes

- `is_valid(hashed_password: bytes, password: str) -> bool`:
  - Validates if a password matches its hashed version
  - Uses bcrypt's constant-time comparison

### 3. Database Connection
- `get_db() -> MySQLConnection`:
  - Creates secure database connections using environment variables
  - Requires database credentials to be set as environment variables

### 4. Logging
- Custom `RedactingFormatter` for logging:
  - Automatically redacts configured PII fields
  - Standardized log format with timestamp
  - Prevents log propagation to other loggers

## Environment Variables

Required for database connection:
- `PERSONAL_DATA_DB_USERNAME` (default: 'root')
- `PERSONAL_DATA_DB_PASSWORD` (default: '')
- `PERSONAL_DATA_DB_HOST` (default: 'localhost')
- `PERSONAL_DATA_DB_NAME` (required)

## Usage

```python
from filtered_logger import get_db, get_logger, hash_password, is_valid

# Password handling
hashed = hash_password("MyPassword")
print(is_valid(hashed, "MyPassword"))  # True

# Database logging
logger = get_logger()
db = get_db()
# ... execute queries ...