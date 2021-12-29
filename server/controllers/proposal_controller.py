import connexion
import six

from server.models.proposal import Proposal  # noqa: E501
from server import util
from server.scripts.proposalList import getProposals

def get_proposals(timeblock, platforms):  # noqa: E501
    """Gets List of Proposals

     # noqa: E501

    :param timeblock: Querying proposals over the last [timeblock] seconds
    :type timeblock: int

     # noqa: E501

    :param platforms: Platform(s) to get proposals from, must be comma-separated string
    :type platforms: string

    :rtype: List[Proposal]
    """
    if not isinstance(timeblock, int) or not isinstance(platforms, str):
        return
        
    if timeblock < 0:
        return
    proposals = []
    if platforms == '':
        proposals = getProposals(timeblock, [])
    else:
        queryPlatforms = platforms.strip(' ').split(',')
        validPlatforms = []
        for p in queryPlatforms:
            if p.isalpha():
               validPlatforms.append(p.lower())
        if len(validPlatforms) > 0:
            proposals = getProposals(timeblock, validPlatforms)
    
    return {"proposals": proposals}
    return 'do some magic!'
