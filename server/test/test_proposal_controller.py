# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from server.models.proposal import Proposal  # noqa: E501
from server.test import BaseTestCase


class TestProposalController(BaseTestCase):
    """ProposalController integration test stubs"""

    def test_get_proposals(self):
        """Test case for get_proposals

        Gets List of Proposals
        """
        query_string = [('timeblock', 24*60*60), ('platforms', '')]
        response = self.client.open(
            '/proposal/getProposals',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
