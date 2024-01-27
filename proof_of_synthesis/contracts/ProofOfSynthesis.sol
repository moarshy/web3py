// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract ProofOfSynthesis {
    struct Synthesis {
        uint256 id;
        string description;
        string synthesisSteps;
        string equipmentAndReagents;
        string analysisResults;
        string metadataURI;
        address creator;
    }

    uint256 public synthesisCount;
    mapping(uint256 => Synthesis) public syntheses;

    function addSynthesis(
        string memory _description,
        string memory _synthesisSteps,
        string memory _equipmentAndReagents,
        string memory _analysisResults,
        string memory _metadataURI
    ) public {
        synthesisCount++;
        syntheses[synthesisCount] = Synthesis(
            synthesisCount,
            _description,
            _synthesisSteps,
            _equipmentAndReagents,
            _analysisResults,
            _metadataURI,
            msg.sender
        );
    }

    function updateSynthesis(
        uint256 _id,
        string memory _description,
        string memory _synthesisSteps,
        string memory _equipmentAndReagents,
        string memory _analysisResults,
        string memory _metadataURI
    ) public {
        Synthesis storage synthesis = syntheses[_id];
        require(msg.sender == synthesis.creator, "Only the creator can modify this record");
        
        synthesis.description = _description;
        synthesis.synthesisSteps = _synthesisSteps;
        synthesis.equipmentAndReagents = _equipmentAndReagents;
        synthesis.analysisResults = _analysisResults;
        synthesis.metadataURI = _metadataURI;
    }

    function retrieveSynthesis(uint256 _id)
        public
        view
        returns (
            uint256,
            string memory,
            string memory,
            string memory,
            string memory,
            string memory,
            address
        )
    {
        Synthesis storage synthesis = syntheses[_id];
        return (
            synthesis.id,
            synthesis.description,
            synthesis.synthesisSteps,
            synthesis.equipmentAndReagents,
            synthesis.analysisResults,
            synthesis.metadataURI,
            synthesis.creator
        );
    }

    function retrieveSyntheses() public view returns (Synthesis[] memory) {
        Synthesis[] memory _syntheses = new Synthesis[](synthesisCount);
        for (uint256 i = 0; i < synthesisCount; i++) {
            Synthesis storage synthesis = syntheses[i + 1];
            _syntheses[i] = synthesis;
        }
        return _syntheses;
    }

    function getNumberOfSyntheses() public view returns (uint256) {
        return synthesisCount;
    }


}
