import os
import time
import json
import coin_mappings
import abi_json
from web3 import Web3
from web3 import HTTPProvider

rpc_endpoint = "https://mainnet.infura.io/v3/<your-token>"
w3 = Web3(HTTPProvider(rpc_endpoint))

_time = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"started at {_time}")
for coin in coin_mappings.mappings.items():
    token_contract = coin[1]["token_contract"]
    exchange_contract = coin[1]["exchange_contract"]

    eth_balance = int(w3.eth.getBalance(exchange_contract))
    coin_balance = int(
        w3.eth.contract(token_contract, abi=abi_json.abi)
        .functions.balanceOf(exchange_contract)
        .call()
    )
    with open(os.path.join("./data/", coin[0]), "a") as file:
        file.write(
            "\n"
            + json.dumps(
                {"time": _time, "eth_b": eth_balance, "coin_b": coin_balance,}
            )
        )
print(f"finished at {time.strftime('%Y-%m-%d %H:%M:%S')}")
