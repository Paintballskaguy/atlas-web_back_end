#!/usr/bin/env python3
"""
This module contains unit tests for the client module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        Args:
            org_name: Name of the organization to test
            mock_get_json: Mock for get_json function
        """
        test_payload = {"name": org_name, "id": 123}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)

        result = client.org

        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        self.assertEqual(result, test_payload)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns the correct list of repositories
        """
        test_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": None}
        ]
        test_repos_url = "https://api.github.com/orgs/testorg/repos"

        mock_get_json.return_value = test_repos_payload

        with patch('client.GithubOrgClient._public_repos_url',
                  new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = test_repos_url

            client = GithubOrgClient("testorg")

            repos = client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)

            mock_repos_url.assert_called_once()

            mock_get_json.assert_called_once_with(test_repos_url)


if __name__ == '__main__':
    unittest.main()
