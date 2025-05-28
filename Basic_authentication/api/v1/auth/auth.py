#!/usr/bin/env python3
""" Auth module for API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required for the given path

        Args:
            path: The path to check
            excluded_paths: List of paths that don't require authentication

        Returns:
            bool: False if path is in excluded_paths, True otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # check that path ends in /
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                if normalized_path == excluded_path:
                    return False
            else:
                if normalized_path == excluded_path + '/':
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the request

        Args:
            request: Flask request object

        Returns:
            str: None for now, will be implemented later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the request

        Args:
            request: Flask request object

        Returns:
            User: None for now, will be implemented later
        """
        return None
