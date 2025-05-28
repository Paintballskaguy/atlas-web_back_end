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
        """Check if authentication is required"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # Normalize path and excluded_paths by adding trailing slash if needed
        path = path if path.endswith('/') else path + '/'

        # Check if normalized path is in excluded_paths
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == (excluded_path if excluded_path.endswith('/') else excluded_path + '/'):
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
