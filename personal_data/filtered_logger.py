#!/usr/bin/env python3
"""
Module for filtering sensitive data in log messages and secure database connections.

This module provides:
- PII redaction in log messages
- Secure database connection handling
- Custom logging formatter for sensitive data
"""

import re
import os
from typing import List, Tuple
import logging
import mysql.connector
from mysql.connector.connection import MySQLConnection


"""
Define the PII fields from user_data.csv that should be redacted
"""

PII_FIELDS: Tuple[str, ...] = (
    "name", "email", "phone", "ssn", "password"
)


def get_db() -> MySQLConnection:
    """
    Creates a secure connection to the MySQL
    database using environment variables.

    Returns:
        A MySQLConnection object to interact with the database

    Environment Variables:
        PERSONAL_DATA_DB_USERNAME: Database username (default: 'root')
        PERSONAL_DATA_DB_PASSWORD: Database password (default: '')
        PERSONAL_DATA_DB_HOST: Database host (default: 'localhost')
        PERSONAL_DATA_DB_NAME: Database name (required)
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    if not db_name:
        raise ValueError(
            "PERSONAL_DATA_DB_NAME environment variable is required")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
     obscure specified fields in a log message by
    replacing them with a redaction string.

    Args:
        fields: List of field names to obfuscate
        redaction: String to replace sensitive data with
        message: Original log message containing fields to obfuscate
        separator: Character that separates fields in the log message

    Returns:
        The log message with specified fields obfuscated
    """
    pattern = rf'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, rf'\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class for filtering sensitive log information."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified log record after redacting sensitive fields.

        Args:
            record: The log record to be formatted

        Returns:
            The formatted and redacted log message
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """Creates and configs a logger for handing user data
    with PII redactions.

    Returns:
        logging.Logger: configured Logger object named 'user_data'
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger
