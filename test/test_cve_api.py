"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.cve_api import CveApi  # noqa: E501


class TestCveApi(unittest.TestCase):
    """CveApi unit test stubs"""

    def setUp(self):
        self.api = CveApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cve_get_cve_detail(self):
        """Test case for cve_get_cve_detail

        getCveDetail cve  # noqa: E501
        """
        pass

    def test_cve_get_cve_list(self):
        """Test case for cve_get_cve_list

        getCveList cve  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()