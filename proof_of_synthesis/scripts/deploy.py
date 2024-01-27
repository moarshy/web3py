from brownie import ProofOfSynthesis, accounts, config

def deploy_proof_of_synthesis():
    account = get_account()
    proof_of_synthesis = ProofOfSynthesis.deploy({"from": account})
    print("Contract deployed to:", proof_of_synthesis.address)
    return proof_of_synthesis

def get_account():
    return accounts[0]  # Modify this if you're using a different account

def add_synthesis(proof_of_synthesis, account):
    tx = proof_of_synthesis.addSynthesis(
        "Description 1",
        "Synthesis Steps 1",
        "Equipment and Reagents 1",
        "Analysis Results 1",
        "metadataURI1",
        {"from": account}
    )
    tx.wait(1)
    print("Synthesis added")

def update_synthesis(proof_of_synthesis, account):
    tx = proof_of_synthesis.updateSynthesis(
        1,  # Assuming you want to update the first record
        "Updated Description",
        "Updated Synthesis Steps",
        "Updated Equipment and Reagents",
        "Updated Analysis Results",
        "updatedMetadataURI",
        {"from": account}
    )
    tx.wait(1)
    print(f"Synthesis Updated: {tx}")

def retrieve_synthesis(proof_of_synthesis):
    synthesis = proof_of_synthesis.retrieveSynthesis(1)  # Retrieving the first record
    print(f"Synthesis Retrieved: {synthesis}")

def retrieve_syntheses(proof_of_synthesis):
    syntheses = proof_of_synthesis.retrieveSyntheses()
    print(f"All Syntheses: {syntheses}")

def get_number_of_syntheses(proof_of_synthesis):
    count = proof_of_synthesis.getNumberOfSyntheses()
    print(f"Number of Syntheses: {count}")

def main():
    proof_of_synthesis = deploy_proof_of_synthesis()
    account = get_account()
    add_synthesis(proof_of_synthesis, account)
    retrieve_synthesis(proof_of_synthesis)
    update_synthesis(proof_of_synthesis, account)
    retrieve_synthesis(proof_of_synthesis)
    retrieve_syntheses(proof_of_synthesis)
    get_number_of_syntheses(proof_of_synthesis)

if __name__ == "__main__":
    main()
