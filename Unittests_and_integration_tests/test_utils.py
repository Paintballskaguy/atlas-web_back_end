#!/usr/bin/env python3
"""
This module contains unit tests for the utils module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for the access_nested_map function in utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """
        Test that access_nested_map raises a KeyError with expected message
        for invalid paths.
        Args:
            nested_map: A nested dictionary
            path: Tuple representing the invalid path
            expected_message: The expected error message
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)

    class TestGetJson(unittest.TestCase):
        """
        Test class for the get_json function in utils module.
        """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected result without making actual HTTP calls.
        Args:
            test_url: URL to mock
            test_payload: Expected JSON payload
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response) as mock_get:
            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)

    class TestMemoize(unittest.TestCase):
        """
        Test class for the memoize decorator in utils module.
        """

    def test_memoize(self):
        """
        Test that memoize decorator caches the result properly.
        """
        class TestClass:
            """
            Test class with memoized property for testing.
            """

            def a_method(self):
                """Method to be memoized."""
                return 42

            @memoize
            def a_property(self):
                """Memoized property that calls a_method."""
                return self.a_method()

        test_instance = TestClass()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
