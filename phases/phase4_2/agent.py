import requests




def fetch_sources_from_relay():
    url = "http://127.0.0.1:8000/sources"
    # The agent sends the secret key to get past the relay's security
    headers = {"X-Agent-Secret": "couple-bands"}

    response = requests.get(url, headers=headers)
    return response.json()


print(fetch_sources_from_relay())
