"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.lockfile_api import LockfileApi  # noqa: E501


class TestLockfileApi(unittest.TestCase):
    """LockfileApi unit test stubs"""

    def setUp(self):
        self.api = LockfileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_lockfile_add_lockfile(self):
        """Test case for lockfile_add_lockfile

        addLockfile lockfile  # noqa: E501
        """
        pass

    def test_lockfile_delete_lockfile(self):
        """Test case for lockfile_delete_lockfile

        deleteLockfile lockfile  # noqa: E501
        """
        pass

    def test_lockfile_get_lockfile_detail(self):
        """Test case for lockfile_get_lockfile_detail

        getLockfileDetail lockfile  # noqa: E501
        """
        pass

    def test_lockfile_get_lockfile_list(self):
        """Test case for lockfile_get_lockfile_list

        getLockfileList lockfile  # noqa: E501
        """
        pass

    def test_lockfile_update_lockfile(self):
        """Test case for lockfile_update_lockfile

        updateLockfile lockfile  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
