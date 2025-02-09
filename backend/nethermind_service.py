import requests

NETHERMIND_RPC_URL = "http://localhost:8000"  

def get_contract_execution(contract_address):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getCode",
        "params": [contract_address, "latest"],
        "id": 1
    }
    response = requests.post(NETHERMIND_RPC_URL, json=payload)
    return response.json()

# Example usage
contract_address = "0xYourSmartContractAddress"
print(get_contract_execution(contract_address))
