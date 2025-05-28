#!/usr/bin/env python3
""" BasicAuth module
"""
from api.v1.auth.auth import Auth
from typing import Union


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth
    """
    def extract_base64_authorization_header(
        self,
        authorization_header: str) -> Union[str, None]:
        """Extracts the Base64 part of the Authorization header for Basic Auth

        Args:
            authorization_header: The Authorization header string

        Returns:
            str: The Base64 part of the header if valid, None otherwise
        """

        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]
