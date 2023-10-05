import requests


def print_transfers(transaction_hash: str):
    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash={transaction_hash}&apikey=YourApiKeyToken"

    try:
        response = requests.get(url=url)

        body = response.json()

        logs = body["result"]["logs"]

        print(logs)

        return logs

    except Exception as error:
        print(f"Error while fetching data: {error}")

        return None


print_transfers("0x3fbb21da357fdd74a12319ee423b4f30829030ba53b1d8d9e005c0da138e2263")
