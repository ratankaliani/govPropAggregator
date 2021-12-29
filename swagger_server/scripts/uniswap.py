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
        query = """query {
            
            proposals(orderBy: endBlock, orderDirection: desc) {
                id
                status
                endBlock
                description
            
            }
        }"""


        response = requests.post(url, json = {'query': query}, headers=header) 
        
        


        blockNum = Uniswap.getBlockNumber()

        data1 = response.json()['data']
        # print(data)


        # Arr00 API
        url = ("https://uni.vote/api/governance/proposals")
        header = {"Authorization": "hibnn:11111:77788777YT666:CAL1"} 
        response = requests.get(url, headers=header)
        data2 = response.json()
        # print(data2)

        total_entries = data2['pagination_summary']['total_entries']

        params = {
            'page_size': total_entries
        }
        url = ("https://api.compound.finance/api/v2/governance/proposals")
        header = {"Authorization": "hibnn:11111:77788777YT666:CAL1"} 
        response = requests.get(url, headers=header, params=params) 
        proposals = []

        # # Can use in future to collect data on all proposals
        # num_pages = data['pagination_summary']['total_pages']

        # # Processing Proposals
        for i in range(len(data1["proposals"])):
        # for proposal in data["proposals"]:
            # endBlock, id
            proposal1 = data1["proposals"][i]
            

            id = proposal1["id"]
            platform = "Uniswap"
            endBlock = int(proposal1['endBlock'])
            # Need to get title added to Uniswap Subgraph
            
            # title, url, state
            proposal2 = data2["proposals"][i]
            title = proposal2["title"]
            state = proposal2["state"]["value"]
            state = state.lower()
            link = proposal2["uniswap_url"]
            endTime = int(time.time() + 13.5 * (int(endBlock) - blockNum))

            # No TxHash
            # print(endTime)
            proposals.append(Proposal(id, platform, title, endTime, None, state, link))
        # print(proposals)
        return proposals

    # print(getProposals())