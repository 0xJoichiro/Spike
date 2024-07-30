

{
    "contest_id": "332",
    "scope": "399 nSLOC",
    "num_issues": 3,
    "nsloc_num": 399,
    "rating": 1197,
    "status": "No"
  },
  {
    "contest_id": "82",
    "scope": "402 nSLOC",
    "num_issues": 4,
    "nsloc_num": 402,
    "rating": 1608,
    "status": "No"
  },
  {
    "contest_id": "285",
    "scope": "916 nSLOC",
    "num_issues": 2,
    "nsloc_num": 916,
    "rating": 1832,
    "status": "No"
  },
  {
    "contest_id": "100",
    "scope": "769 nSLOC",
    "num_issues": 7,
    "nsloc_num": 769,
    "rating": 5383,
    "status": "No"
  },


also clear out prev mess



---------------------------------------------------------


## Contest 285 - Tokensoft Distributor Contracts Update

- https://github.com/0xJoichiro/2024-05-tokensoft-distributor-contracts-update
- https://audits.sherlock.xyz/contests/285

<img src="image-10.png" alt="alt text" height="50%" width="50%">


### Valid - (2), Invalid 42

-  [M1 - PerAddressTrancheVestingMerkleDistributor.claim always reverts because it checks the Merkle proof incorrectly](https://github.com/sherlock-audit/2024-05-tokensoft-distributor-contracts-update-judging/issues/9)
-  [M2 - PerAddressTrancheVestingMerkleDistributor.claim always reverts because it attempts to decode a bytes(0) as a Tranche[].](https://github.com/sherlock-audit/2024-05-tokensoft-distributor-contracts-update-judging/issues/64)

#### Summary

-  Both the claim and initializeDistributionRecord methods of PerAddressTrancheVestingMerkleDistributor do not include the tranches when checking the Merkle proof (and do not even accept the tranches as a parameter). Both methods therefore always revert, before the function body is even entered.
-  The PerAddressContinuousVestingMerkleDistributor and PerAddressTrancheVestingMerkleDistributor contract will always revert due to new bytes(0) pass to _executeClaim function.Root cause : start, cliff, end values are not encoded when computing getVestedFraction and it will revert when it tries to decode the zero bytes data into start, cliff, end


#### POC - TestCaseFile

-  
-  

#### Giveaways


- merkle tree function is not getting tranches as input
- We know from PerAddressTrancheVestingMerkle that the Merkle trees for this kind of distributor include the list of tranches for each address
- Users could potentially provide custom tranche data that allows for immediate claiming of the entire allocated amount, bypassing any intended vesting schedule.
- LHS != RHS check to be done
- tranches and merkleproof
- ERC165
- merkle proof
- membership in merkleroot
- import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
- import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";
- import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
- import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
- import {Clones} from "@openzeppelin/contracts/proxy/Clones.sol";



2nd ->
- https://github.com/sherlock-audit/2024-05-tokensoft-distributor-contracts-update-judging/issues/26
- https://github.com/sherlock-audit/2024-05-tokensoft-distributor-contracts-update-judging/issues/29
- https://github.com/sherlock-audit/2024-05-tokensoft-distributor-contracts-update-judging/issues/32
- 39 , 56,58 63 64 45 20 8 11
 

---------------------------------------------------------


## Contest 100 - Tokensoft

- https://audits.sherlock.xyz/contests/100

<img src="image-11.png" alt="alt text" height="50%" width="50%">

### Valid - (7), Invalid 164

-  [M1 - Because of rounding issues, users may not be able to withdraw airdrop tokens if their claim has been adjust()'ed upwards](https://github.com/sherlock-audit/2023-06-tokensoft-judging/issues/56)
-  [M2 - Logic error occurs when executing a claim, if the beneficiary was adjusted before](https://github.com/sherlock-audit/2023-06-tokensoft-judging/issues/195)
-  [M3 - In PriceTierVesting there is no check if the Sequenzer for L2s is up when calling the oralce](https://github.com/sherlock-audit/2023-06-tokensoft-judging/issues/38)
-  [M4 - SetTotal revert due to allowance being set from non-zero value to non-zero value](https://github.com/sherlock-audit/2023-06-tokensoft-judging/issues/119)
-  [M5 - setVoteFactor() does not change existing supply of votes. As a result, some may be unable to withdraw](https://github.com/sherlock-audit/2023-06-tokensoft-judging/issues/133)
-  [M6 - Lack of relayer fee payment](https://github.com/sherlock-audit/2023-06-tokensoft-judging/issues/97)
-  [H1 - Distribution records can be initialised repeatedly to gain infinite voting power](https://github.com/sherlock-audit/2023-06-tokensoft-judging/issues/180)

#### Summary

-  In order for a user to withdraw their claim, they must have enough voting tokens. However, because of rounding issues, if their voting shares are granted in multiple stages, namely by the owner adjust()-ing their share upwards, they will not have enough.
-  .
-  In the current implementation, several contracts include PriceTierVestingSale_2_0 and Distributor use block.timestamp to calculate claimable token amounts and price tiers end time.
However, it's vulnerable when l2 sequencer go down cause that block.timestamp is unusable. L2 chains like arbitrum and optimism upgrade their sequencer occasionally, such as the recent optimism bedrock upgrade cause the sequencer can't be able to process transactions for several hours. Or l2 sequencer bug could also cause transactions in stuck, such as arbitrum sequencer bug. So it's necessary to implement a mechanism to handle this issue in some abnormal conditions.
- When using OpenZeppelin's safeApprove() function, if it is already approved, and a new safeApprove() is attempted with a non-zero value, it will result in a revert.This occurs in the _setTotal function, which prevents updating setTotal always.safeApprove should only be called when setting an initial allowance, or when resetting it to zero. To increase and decrease it, use 'safeIncreaseAllowance' and 'safeDecreaseAllowance'
- Upon initialization of a user's DistributionRecord, they are minted voting power based on the current voteFactor value. Upon claiming tokens, their voting power is burned based on the current votefactor. Therefore, if the voteFactor were to increase between these actions by calling setVoteFactor(), users would not be able to claim their full amount of tokens.
- According to the Connext docs, the relayer fee is a charge imposed by relayers for executing transactions on the destination chain, which can be paid in either the native asset of the origin or the transacting asset. However, the current implementation of the CrosschainDistributor._settleClaim does not include passing the relayer fee at all.
- 

#### POC - TestCaseFile

-  

#### Giveaways

- rounding errors up and down
- mismatching in code getting value in 2 different ways intro a bug
- L2 sequencer
- CanonicalTransactionChain
- stale price feed - https://ethereum.stackexchange.com/questions/133242/how-future-resilient-is-a-chainlink-price-feed/133843#133843
- safeapprove 'safeIncreaseAllowance' and 'safeDecreaseAllowance'
- vote supply and vote token should increase and decrease together




<!-- ---------------------------------------------------------


## Contest Number - Name


<img src="image-7.png" alt="alt text" height="50%" width="50%">


### Valid - (1), Invalid 103

-  

#### Summary

-  

#### POC - TestCaseFile

-  

#### Giveaways

 -->