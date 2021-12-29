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
        total_entries = data['pagination_summary']['total_entries']

        params = {
            'page_size': total_entries
        }
        url = ("https://api.compound.finance/api/v2/governance/proposals")
        header = {"Authorization": "hibnn:11111:77788777YT666:CAL1"} 
        response = requests.get(url, headers=header, params=params) 
        # print(response.json())

        data = response.json()
        proposals = []
        # Processing Proposals
        for proposal in data["proposals"]:
            
            title = proposal["title"]
            # print(title)
            id = proposal["id"]
            platform = "Compound"
            
            state = proposal["states"][-1]
            endTime = state["end_time"]
            if endTime is None:
                endTime = state['start_time']
            txHash = state["trx_hash"]
            link = "https://compound.finance/governance/proposals/" + str(id)
            status = state['state']
            
            proposals.append(Proposal(id, platform, title, endTime, txHash, status, link))
        # print(proposals)
        return proposals

    # print(getProposals())

