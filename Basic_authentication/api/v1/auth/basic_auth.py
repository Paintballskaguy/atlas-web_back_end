#!/usr/bin/env python3
""" BasicAuth module
"""
from api.v1.auth.auth import Auth
from typing import Union, Tuple
import base64


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

        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> Union[str, None]:
        """Decodes a Base64 encoded authorization header

        Args:
            base64_authorization_header: Base64 encoded string

        Returns:
            str: Decoded value as UTF-8 string or None if invalid
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Extracts user credentials from decoded Base64 string"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':', 1)
        return (email, password)
