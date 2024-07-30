# Notes

---------------------------------------------------------


## Contest 326


<img src="https://gray-accessible-centipede-987.mypinata.cloud/ipfs/QmeS7c6f5P4m7vce9FZzDgxtPjfTLSXwedXfbAhRd9iYH9" alt="alt text" height="50%" width="50%">


### Tools Used

#### cloc work

- Scope 

wallflower-contract-v2/src/shared/Common.sol: 80 lines
wallflower-contract-v2/src/TitlesCore.sol: 119 lines
wallflower-contract-v2/src/graph/TitlesGraph.sol: 145 lines  
wallflower-contract-v2/src/fees/FeeManager.sol: 271 lines
wallflower-contract-v2/src/editions/Edition.sol: 301 lines

#### Aderyn

### Valid (17), Invalid (181)

1. https://github.com/sherlock-audit/2024-04-titles-judging/issues/21
2. https://github.com/sherlock-audit/2024-04-titles-judging/issues/1
3. https://github.com/sherlock-audit/2024-04-titles-judging/issues/4
4. https://github.com/sherlock-audit/2024-04-titles-judging/issues/2
5. https://github.com/sherlock-audit/2024-04-titles-judging/issues/7
6. https://github.com/sherlock-audit/2024-04-titles-judging/issues/16
7. https://github.com/sherlock-audit/2024-04-titles-judging/issues/96
8. https://github.com/sherlock-audit/2024-04-titles-judging/issues/9 -- 
9. https://github.com/sherlock-audit/2024-04-titles-judging/issues/170 -- test_graph_cannot_upgrade 
10. https://github.com/sherlock-audit/2024-04-titles-judging/issues/213 
11. https://github.com/sherlock-audit/2024-04-titles-judging/issues/171
12. https://github.com/sherlock-audit/2024-04-titles-judging/issues/274 --
13. https://github.com/sherlock-audit/2024-04-titles-judging/issues/416 -- 
14. https://github.com/sherlock-audit/2024-04-titles-judging/issues/258 --
15. https://github.com/sherlock-audit/2024-04-titles-judging/issues/353 -- 
16. https://github.com/sherlock-audit/2024-04-titles-judging/issues/322 -- 
17. https://github.com/sherlock-audit/2024-04-titles-judging/issues/285 -- asked for more info


#### POC - TestCaseFile command

``

1. `forge test --mt test_mintPoc -vvv`
2. `forge test --mt test_mintBatchBroken -vvv`
3. `forge test --mt  -vvv`
4. `forge test --mt test_mintBatchBroken -vvv`
5.
6.
7.
8.
9. 
10. test_cannotConfigureEditionMinterRole
11.test_incorrectSupportsInterface
12. `forge test --mt  -vvvvv`
13. `forge test --mt test_maliciousReferrerBricksEdition -vvv`
14.  `forge test --mt test_inconsistentRoyaltyInfo -vvv`
15.
16.  testReferrerOverrideOnNewWork
17.  test_maliciousEditionManagerFrontRunRoyalty



#### Giveaways

- aderyn and cloc working
- ERC2981
- EIP712
- OpenGraph standard
- solady
- openzepplin all
- ERC1967
- https://medium.com/immunefi/how-to-reproduce-a-simple-mev-attack-b38151616cb4 - frontrunning
- create/create2 in zksync
- https://github.com/matter-labs/foundry-zksync
- dos woth contract using revert only
- UUPSUpgradeable


 <!-- ---------------------------------------------------------


## Contest Number - Name


<img src="image-7.png" alt="alt text" height="50%" width="50%">


### Valid - (1), Invalid 103

- 1. 

#### Summary

- 1. 

#### POC - TestCaseFile


- 1. 


#### Giveaways


 -->