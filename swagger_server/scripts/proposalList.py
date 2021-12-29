# import platforms
from swagger_server.scripts.compound import Compound
from swagger_server.scripts.aave import Aave
from swagger_server.scripts.uniswap import Uniswap

import time
from swagger_server.models.proposal import Proposal  # noqa: E501


def getProposals(timeblock):
    # print(timeblock)
    cutoff = time.time() - (timeblock)
    # get Proposals

    compProposals = Compound.getProposalsFast(timeblock)
    aaveProposals = Aave.getProposalsFast(timeblock)
    uniswapProposals = Uniswap.getProposalsFast(timeblock)
    # combine Proposals
    allProposals = []
    allProposals.extend(compProposals)
    allProposals.extend(aaveProposals)
    allProposals.extend(uniswapProposals)
    print("AllProposals length: " + str(len(allProposals)))

    recentProposals = []
    for proposal in allProposals:
        # print(proposal.platform)
        # print(proposal.id)
        # print(proposal.getEndDate())
        # print(proposal.platform)
        # print(proposal.end_time)
        # print(proposal.link)
        if proposal.end_time and proposal.end_time > cutoff:
            recentProposals.append(proposal)
    
    return recentProposals

def test():
    timeblock = (3600 * 24)
    # print(getProposals(timeblock))

# test()