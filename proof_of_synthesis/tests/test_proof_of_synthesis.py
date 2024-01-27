from brownie import ProofOfSynthesis, accounts

def test_deploy():
    account = accounts[0]
    proof_of_synthesis = ProofOfSynthesis.deploy({"from": account})
    assert proof_of_synthesis.address != ""

def test_add_synthesis():
    account = accounts[0]
    proof_of_synthesis = ProofOfSynthesis.deploy({"from": account})
    tx = proof_of_synthesis.addSynthesis("Desc", "Steps", "Equipment", "Results", "URI", {"from": account})
    tx.wait(1)

    assert proof_of_synthesis.synthesisCount() == 1

def test_update_synthesis():
    account = accounts[0]
    proof_of_synthesis = ProofOfSynthesis.deploy({"from": account})
    proof_of_synthesis.addSynthesis("Desc", "Steps", "Equipment", "Results", "URI", {"from": account})

    tx = proof_of_synthesis.updateSynthesis(1, "New Desc", "New Steps", "New Equipment", "New Results", "New URI", {"from": account})
    tx.wait(1)

    updated_synthesis = proof_of_synthesis.syntheses(1)
    assert updated_synthesis[1] == "New Desc"

def test_retrieve_synthesis():
    account = accounts[0]
    proof_of_synthesis = ProofOfSynthesis.deploy({"from": account})
    proof_of_synthesis.addSynthesis("Desc", "Steps", "Equipment", "Results", "URI", {"from": account})

    retrieved_synthesis = proof_of_synthesis.retrieveSynthesis(1)
    assert retrieved_synthesis[1] == "Desc"

def test_retrieve_syntheses():
    account = accounts[0]
    proof_of_synthesis = ProofOfSynthesis.deploy({"from": account})
    proof_of_synthesis.addSynthesis("Desc", "Steps", "Equipment", "Results", "URI", {"from": account})
    proof_of_synthesis.addSynthesis("Desc 2", "Steps 2", "Equipment 2", "Results 2", "URI 2", {"from": account})

    syntheses = proof_of_synthesis.retrieveSyntheses()
    assert len(syntheses) == 2

def test_update_synthesis_unauthorized():
    account1 = accounts[0]
    account2 = accounts[1]
    proof_of_synthesis = ProofOfSynthesis.deploy({"from": account1})
    proof_of_synthesis.addSynthesis("Desc", "Steps", "Equipment", "Results", "URI", {"from": account1})

    try:
        proof_of_synthesis.updateSynthesis(1, "Illegal Update", "Illegal Steps", "Illegal Equipment", "Illegal Results", "Illegal URI", {"from": account2})
        assert False  # This should not happen
    except Exception as e:
        assert "Only the creator can modify this record" in str(e)
