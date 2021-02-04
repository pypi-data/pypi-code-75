# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_file
from pulpcore.client.pulp_file.models.paginatedfile_file_remote_response_list import PaginatedfileFileRemoteResponseList  # noqa: E501
from pulpcore.client.pulp_file.rest import ApiException

class TestPaginatedfileFileRemoteResponseList(unittest.TestCase):
    """PaginatedfileFileRemoteResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedfileFileRemoteResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_file.models.paginatedfile_file_remote_response_list.PaginatedfileFileRemoteResponseList()  # noqa: E501
        if include_optional :
            return PaginatedfileFileRemoteResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_file.models.file/file_remote_response.file.FileRemoteResponse(
                        pulp_href = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        url = '0', 
                        ca_cert = '0', 
                        client_cert = '0', 
                        client_key = '0', 
                        tls_validation = True, 
                        proxy_url = '0', 
                        username = '0', 
                        password = '0', 
                        pulp_labels = pulpcore.client.pulp_file.models.pulp_labels.pulp_labels(), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        download_concurrency = 1, 
                        policy = null, 
                        total_timeout = 0.0, 
                        connect_timeout = 0.0, 
                        sock_connect_timeout = 0.0, 
                        sock_read_timeout = 0.0, 
                        rate_limit = 56, )
                    ]
            )
        else :
            return PaginatedfileFileRemoteResponseList(
        )

    def testPaginatedfileFileRemoteResponseList(self):
        """Test PaginatedfileFileRemoteResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
