# Pull data from here: https://thegraph.com/hosted-service/subgraph/aave/governance-v2

# Ethereum is 6400 blocks a day
# Need to get subgraph on Aave
# Block is 13.5 seconds



import requests 
from swagger_server.models.proposal import Proposal  # noqa: E501
import time
class Aave:
    def getBlockNumber():
        url = ("https://api.blockcypher.com/v1/eth/main")
        response = requests.get(url)
        data = response.json()
        blockNumber = int(data['height'])
        return blockNumber

    def getProposals():
        # Get last block number
        url = ("https://api.thegraph.com/subgraphs/name/aave/governance-v2")
        header = {"Authorization": "hibnn:11111:77788777YT666:CAL1"} 
        # limit at 10 proposals
        query = """query {
            proposals(orderBy: endBlock, orderDirection: desc, first: 10) {
            id
            state
            startBlock
            endBlock
            ipfsHash
            title
            shortDescription
            }
        }"""


        response = requests.post(url, json = {'query': query}, headers=header) 
        


        blockNum = Aave.getBlockNumber()

        data = response.json()['data']
        # print(data)
        proposals = []
        # # Can use in future to collect data on all proposals
        # num_pages = data['pagination_summary']['total_pages']

        # # Processing Proposals
        for proposal in data["proposals"]:
            
            title = proposal["title"]
            id = proposal["id"]
            platform = "Aave"
            ipfsHash = proposal["ipfsHash"]
            startBlock = int(proposal['startBlock'])
            endBlock = int(proposal['endBlock'])
            shortDesc = proposal['shortDescription']
            # state definitions for future extensions
            stateDefinition = {
                "failed": "defeated"
            }
            state = proposal["state"]
            state = state.lower()
            # Standardize states
            if state in stateDefinition.keys():
                state = stateDefinition[state]
                
            link = "https://app.aave.com/#/" + str(id) + "-" + str(ipfsHash)
            endTime = int(time.time() + 13.5 * (int(endBlock) - blockNum))

            # No TxHash
            # print(endTime)
            proposals.append(Proposal(id, platform, title, endTime, None, state, link))
        # print(proposals)
        return proposals

    # print(getProposals())