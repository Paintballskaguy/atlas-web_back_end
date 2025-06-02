#!/usr/bin/env python3
"""
This module contains unit tests for the client module.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Mock requests.get to return payloads based on URL"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            mock = Mock()
            if url.endswith('/orgs/google'):
                mock.json.return_value = cls.org_payload
            elif url.endswith('/orgs/google/repos'):
                mock.json.return_value = cls.repos_payload
            return mock

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos without license filter"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license filter"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), 
                self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
