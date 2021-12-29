# import platforms
from server.scripts.compound import Compound
from server.scripts.aave import Aave
from server.scripts.uniswap import Uniswap

import time
from server.models.proposal import Proposal  # noqa: E501

# Assumes timeblock > 0
# if platforms is empty, query all
# else check if platforms (lowercase) are supported
def getProposals(timeblock, queryPlatforms):

    supportedPlatforms = set(
       [
           'aave',
           'compound',
           'uniswap'
       ] 
    )

    platforms = supportedPlatforms.intersection(queryPlatforms)

    cutoff = time.time() - (timeblock)
    # get all proposals
    queryAll = len(queryPlatforms) == 0
    
    allProposals = []
    if queryAll or 'aave' in platforms: 
        aaveProposals = Aave.getProposalsFast(timeblock)
        allProposals.extend(aaveProposals)
    if queryAll or 'compound' in platforms:
        compProposals = Compound.getProposalsFast(timeblock)
        allProposals.extend(compProposals)
    if queryAll or 'uniswap' in platforms:
        uniswapProposals = Uniswap.getProposalsFast(timeblock)
        allProposals.extend(uniswapProposals)
    
    
    print("AllProposals length: " + str(len(allProposals)))

    recentProposals = []
    for proposal in allProposals:

        if proposal.end_time and proposal.end_time > cutoff:
            recentProposals.append(proposal)
    
    return recentProposals
