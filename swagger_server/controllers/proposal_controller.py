import connexion
import six

from swagger_server.models.proposal import Proposal  # noqa: E501
from swagger_server import util
from swagger_server.scripts.proposalList import getProposals

def get_proposals(timeblock):  # noqa: E501
    """Gets List of Proposals

     # noqa: E501

    :param timeblock: Querying proposals over the last [timeblock] seconds
    :type timeblock: int

    :rtype: List[Proposal]
    """
    if timeblock < 0:
        return
    proposals = getProposals(timeblock)
    return proposals
    return 'do some magic!'
