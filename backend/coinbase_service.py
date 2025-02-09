import requests

COINBASE_API_KEY = "your_api_key_here"
headers = {"Authorization": f"Bearer {COINBASE_API_KEY}"}

def get_user_wallet_balance():
    url = "https://api.coinbase.com/v2/accounts"
    response = requests.get(url, headers=headers)
    return response.json()

# Example usage
print(get_user_wallet_balance())
