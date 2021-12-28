import requests 
from swagger_server.models.proposal import Proposal  # noqa: E501

class Compound:

    def getBlockNumber():
        url = ("https://api.blockcypher.com/v1/eth/main")
        response = requests.get(url)
        data = response.json()
        blockNumber = int(data['height'])
        return blockNumber

    def getProposals():
        url = ("https://api.compound.finance/api/v2/governance/proposals")
        header = {"Authorization": "hibnn:11111:77788777YT666:CAL1"} 
        response = requests.get(url, headers=header) 
        # print(response.json())

        data = response.json()
        proposals = []
        # Can use in future to collect data on all proposals
        num_pages = data['pagination_summary']['total_pages']

        # Processing Proposals
        for proposal in data["proposals"]:
            
            title = proposal["title"]
            # print(title)
            id = proposal["id"]
            platform = "Compound"


            state = proposal["states"][-1]
            endTime = state["end_time"]
            txHash = state["trx_hash"]
            link = "https://compound.finance/governance/proposals/" + str(id)
            
            proposals.append(Proposal(id, platform, title, endTime, txHash, state, link))
        print(proposals)
        return proposals

    # print(getProposals())

