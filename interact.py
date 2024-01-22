import os
import json
from dotenv import load_dotenv
from web3 import Web3


# Load env variables
load_dotenv()

# Get address and abi from json file
with open("deployed_contract.json") as file:
    data = json.load(file)
    abi = data['abi']
    contract_address = data['contract_address']

# Connec to ganache
GANACHE_PORT = os.getenv("GANACHE_PORT", None)
ADDRESS = os.getenv("ADDRESS", None)
PRIVATE_KEY = os.getenv("PRIVATE_KEY", None)

# print all env variables
print(f"GANACHE_PORT: {GANACHE_PORT}")
print(f"ADDRESS: {ADDRESS}")

if GANACHE_PORT:
    w3 = Web3(Web3.HTTPProvider(f"http://0.0.0.0:{GANACHE_PORT}"))
else:
    raise Exception("GANACHE_PORT environment variable not set")

# Create the contract in python
simple_storage = w3.eth.contract(address=contract_address, abi=abi)

# Call a function
print(simple_storage.functions.retrieve().call())

# Send a transaction
print("Updating contract...")
store_transaction = simple_storage.functions.store(15).build_transaction(
    {
        "chainId": w3.eth.chain_id,
        "from": ADDRESS,
        "nonce": w3.eth.get_transaction_count(ADDRESS),
    }
)
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=PRIVATE_KEY
)

send_store_txn = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
print(f"send_store_txn: {send_store_txn.hex()}")

tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn)
print(f"tx_receipt: {tx_receipt}")

print(simple_storage.functions.retrieve().call())