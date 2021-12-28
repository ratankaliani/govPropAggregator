# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.proposal import Proposal  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProposalController(BaseTestCase):
    """ProposalController integration test stubs"""

    def test_get_proposals(self):
        """Test case for get_proposals

        Gets List of Proposals
        """
        query_string = [('timeblock', 24*60*60)]
        response = self.client.open(
            '/ratan00/ProposalBot/1.0.0/proposal/getProposals',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
