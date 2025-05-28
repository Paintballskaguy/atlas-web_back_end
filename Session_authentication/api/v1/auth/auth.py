#!/usr/bin/env python3
""" Auth module for API authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize the path by ensuring it ends with /
        normalized_path = path if path.endswith('/') else path + '/'

        # Check against each excluded path
        for excluded_path in excluded_paths:
            # Normalize the excluded path
            normalized_excluded = excluded_path if excluded_path.endswith('/') else excluded_path + '/'
            if normalized_path == normalized_excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Get Authorization header from request"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Get current user from request (always None in base Auth)"""
        return None

    def session_cookie(self, request=None):
        """Returns the value of session cookie from request"""
        if request is None:
            return None

        session_name = getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
