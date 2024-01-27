# Web3 Project

## Installation
To install the Web3 project, follow these steps:

1. Clone the Repository

First, clone the repository to your local machine:
```bash
git clone THIS_REPO
cd THIS_REPO
```

2. Install Ganache

[Ganache](https://trufflesuite.com/ganache/) is a personal blockchain for Ethereum development you can use to deploy contracts, develop applications, and run tests. It is available for Windows, Mac, and Linux.

Download and install Ganache from the official website:

https://trufflesuite.com/ganache/

3. Install Python Dependencies

This project requires certain Python dependencies. Install them using pip:
```bash
pip install -r requirements.txt
```

4. Prepare the .env file

## Usage
To use the project, run the following command:
```bash
python deploy.py
```

To interact with the deployed contract:
```bash
python interact.py
```

### Errors installing eth-brownie

What worked
```bash
python=3.8
pip install "cython<3.0.0" && pip install --no-build-isolation eth-brownie
```

### Deploying ProofOfSynthesis with eth-brownie
1. Install eth-brownie

If you haven't installed eth-brownie, use the following command:

```bash
pip install "cython<3.0.0" && pip install --no-build-isolation eth-brownie
```

2. Navigate to the Project Directory
```bash
cd path/to/proof_of_synthesis
```
Replace path/to/proof_of_synthesis with the actual path to your proof_of_synthesis project directory.

3. Compile the Smart Contract
Compile the smart contract using Brownie:
```bash
brownie compile
```
This step will compile all Solidity files in your project.

4. Deploy the Contract
Execute the deployment script located in the scripts directory:

```bash
brownie run scripts/deploy
```
This command will run the deploy.py script, which handles the deployment of your ProofOfSynthesis contract and interactions with the contract.