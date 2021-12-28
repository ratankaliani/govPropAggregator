# Pull data from here: https://api.thegraph.com/subgraphs/name/arr00/uniswap-governance-v2


# Ethereum is 6400 blocks a day
# Block is 13.5 seconds



import requests 
from swagger_server.models.proposal import Proposal  # noqa: E501
import time
import re
class Uniswap:
    def getBlockNumber():
        url = ("https://api.blockcypher.com/v1/eth/main")
        response = requests.get(url)
        data = response.json()
        blockNumber = int(data['height'])
        return blockNumber

    def getProposals():
        # Get last block number
        url = ("https://api.thegraph.com/subgraphs/name/arr00/uniswap-governance-v2")
        header = {"Authorization": "hibnn:11111:77788777YT666:CAL1"} 
        # limit at 10 proposals
        query = """query {
            
            proposals(orderBy: endBlock, orderDirection: desc, first: 10) {
                id
                status
                endBlock
                description
            
            }
        }"""


        response = requests.post(url, json = {'query': query}, headers=header) 
        


        blockNum = Uniswap.getBlockNumber()

        data = response.json()['data']
        # print(data)
        proposals = []
        # # Can use in future to collect data on all proposals
        # num_pages = data['pagination_summary']['total_pages']

        # # Processing Proposals
        for proposal in data["proposals"]:
            
            id = proposal["id"]
            platform = "Uniswap"
            endBlock = int(proposal['endBlock'])
            # Need to get title added to Uniswap Subgraph
            desc = proposal['description']
            # Desc Formatting
            # Check if markdown
            # nL = desc.find("\n")
            # ind = desc.find("##")
            # minInd = min(nL, ind)
            # newStr = desc[: minInd]
            # pattern = re.compile('#')
            # title = pattern.sub('', newStr)
            # print(title)
            # state definitions for future extensions
            stateDefinition = {
                "canceled": -2,
                "failed": -1,
                "pending": 0,
                "active": 1,
                "succeeded": 2,
                "queued": 4,
                "executed": 5
            }
            state = proposal["status"]
            state = state.lower()
            # Only for active & pending proposals for right now (bot)
            # print(stat)
            link = "https://sybil.org/#/proposals/uniswap/" + str(id)
            endTime = int(time.time() + 13.5 * (int(endBlock) - blockNum))

            # No TxHash
            # print(endTime)
            proposals.append(Proposal(id, platform, None, endTime, None, state, link))
        # print(proposals)
        return proposals

    # print(getProposals())