#!/usr/bin/env python3
"""
Module for filtering and obfuscating sensitive data in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message by replacing them with a redaction string.

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