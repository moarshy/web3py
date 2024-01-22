import os
import json
from dotenv import load_dotenv
from web3 import Web3
from solcx import compile_standard, install_solc

# Load env variables
load_dotenv()

# Install solc version (if not already installed)
install_solc("0.6.0")


# Compile solidity code
with open("./SimpleStorage.sol") as file:
    simple_storage_contract = file.read()

# Solidity source code
compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_contract}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },

    },
    solc_version="0.6.0",
)

# print
# print(compile_sol)

# write to json file
with open("compiled_code.json", "w") as file:
    json.dump(compile_sol, file)

# get bytecode
bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Connec to ganache
GANACHE_PORT = os.getenv("GANACHE_PORT", None)
ADDRESS = os.getenv("ADDRESS", None)
PRIVATE_KEY = os.getenv("PRIVATE_KEY", None)

# print all env variables
print(f"GANACHE_PORT: {GANACHE_PORT}")
print(f"ADDRESS: {ADDRESS}")

if GANACHE_PORT:
    web3 = Web3(Web3.HTTPProvider(f"http://0.0.0.0:{GANACHE_PORT}"))
else:
    raise Exception("GANACHE_PORT environment variable not set")

# Create the contract in python
SimpleStorage = web3.eth.contract(abi=abi, bytecode=bytecode)

# Get the latest transaction
nonce = web3.eth.get_transaction_count(ADDRESS)

# Submit the transaction that deploys the contract
transaction = SimpleStorage.constructor().build_transaction(
    {
        "chainId": web3.eth.chain_id,
        "gasPrice": web3.eth.gas_price,
        "from": ADDRESS,
        "nonce": nonce,
    }
)
print(f"transaction: {transaction}")

# Sign the transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
print(f"signed_txn: {signed_txn}")

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(f"tx_hash: {tx_hash}")

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"tx_receipt: {tx_receipt}")
print(f"Contract deployed to {tx_receipt.contractAddress}")

# Save the contract address and abi in a json file
data = {
    "abi": abi,
    "contract_address": tx_receipt.contractAddress,
}
with open("deployed_contract.json", "w") as file:
    json.dump(data, file)