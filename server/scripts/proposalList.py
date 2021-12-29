# import platforms
from server.scripts.compound import Compound
from server.scripts.aave import Aave
from server.scripts.uniswap import Uniswap

import time
from server.models.proposal import Proposal  # noqa: E501
from heapq import merge
from operator import itemgetter


# function for meging k arrays
def mergeK(arr, k):
     
    l = arr[0]
    for i in range(k-1):
        l = list(merge(l, arr[i + 1], key = itemgetter("end_time")))
    return l


# Assumes timeblock > 0
# if platforms is empty, query all
# else check if platforms (lowercase) are supported
def getProposals(timeblock, queryPlatforms):

    queryAll = len(queryPlatforms) == 0

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
    
    if queryAll:
        numPlatforms = len(supportedPlatforms)
    else:
        numPlatforms = len(platforms)
    
    allProposals = []

    # Sort K sorted arrays on endTime
    if queryAll or 'aave' in platforms: 
        aaveProposals = Aave.getProposalsFast(timeblock)
        allProposals.append(aaveProposals)
    if queryAll or 'compound' in platforms:
        compProposals = Compound.getProposalsFast(timeblock)
        allProposals.append(compProposals)
    if queryAll or 'uniswap' in platforms:
        uniswapProposals = Uniswap.getProposalsFast(timeblock)
        allProposals.append(uniswapProposals)
    
    allProposals = mergeK(allProposals, numPlatforms)

    
    print("AllProposals length: " + str(len(allProposals)))

    recentProposals = []
    for proposal in allProposals:

        if proposal.end_time and proposal.end_time > cutoff:
            recentProposals.append(proposal)
    

    return recentProposals
