# Sherlock

## Contest 159 - Rio Vesting Escrow
- https://audits.sherlock.xyz/contests/159
- https://github.com/sherlock-audit/2024-01-rio-vesting-escrow/tree/main

<img src="image.png" alt="alt text" height="50%" width="50%">



### Valid - (1), Invalid 103

- 1. [H1 - Destructing VestingEscrow implementation via delegatecall](https://github.com/sherlock-audit/2024-01-rio-vesting-escrow-judging/issues/28)

#### Summary

- 1. By creating a fake IVotingAdaptor, and providing properly-formatted calldata to the implementation contract being passed to each factory, an attacker can gain control via the delegatecall() in order to selfdestruct() each of the factories' implementations, preventing each factory's escrows from functioning further, including the withdrawal of tokens by any party.


#### POC - TestCaseFile

- https://github.com/0xJoichiro/2024-01-rio-vesting-escrow/blob/71abf7b555955e7f1f0ab086172f631ef8acda26/rio-vesting-escrow/test/VestingEscrowFactory.t.sol#L90


---------------------------------------------------------

## Contest 78 - DODO Margin Trading
- https://audits.sherlock.xyz/contests/78
- https://github.com/sherlock-audit/2023-05-dodo/tree/main

<img src="image-1.png" alt="alt text" height="50%" width="50%">


### Valid - (2), Invalid 153

- 1.[M1 - MarginTrading.sol: The whole balance and not just the traded funds are deposited into Aave when a trade is opened](https://github.com/sherlock-audit/2023-05-dodo-judging/issues/72)
- 2.[H1 - Anyone can drain all of the user funds from margin account using external flashloan]()
    


#### Summary

- 1.It's expected by the protocol that funds can be in the MarginTrading contract without being deposited into Aave as margin.We can see this by looking at the `MarginTradingFactory.depositMarginTradingETH` and `MarginTradingFactory.depositMarginTradingERC20` functions.If the user sets margin=false as the parameter, the funds are only sent to the MarginTrading contract but NOT deposited into Aave.
Let's look at the `MarginTrading._openTrade` function that is called when a trade is opened: The whole balance of the token will be deposited into Aave:
- 2.



#### POC - TestCaseFile

- 1.
- 2.



---------------------------------------------------------


## Contest 273 - Alchemix - Optimism Bridging and Reward Routing

- https://audits.sherlock.xyz/contests/273
- https://github.com/sherlock-audit/2024-04-alchemix

<img src="image-2.png" alt="alt text" height="50%" width="50%">

### Valid - (1), Invalid 160

- 1. [H1 - The calculated value for slippage protection in the protocol is inaccurate](https://github.com/sherlock-audit/2024-04-alchemix-judging/issues/30)

#### Summary

- 1. The protocol calculates the slippage protection value based on the price of OP relative to USD and OP relative to ETH, while the intended exchange is for alUSD and alETH. This results in inaccuracies in the calculated slippage protection value.

#### POC - TestCaseFile

- 1. 

---------------------------------------------------------


## Contest 184 - Rubicon Finance

- https://audits.sherlock.xyz/contests/184
- https://github.com/0xJoichiro/2024-02-rubicon-finance

<img src="image-3.png" alt="alt text" height="50%" width="50%">


### Valid - (1), Invalid 73

- 1. [M1 - Rounding error in fee comparison logic resulting in denial of service](https://github.com/sherlock-audit/2024-02-rubicon-finance-judging/issues/51)

#### Summary

- 1. If the pair has set the max fee by the fee controller admin which is "1_000" then depending on the amount to be swapped, the tx can revert due to rounding error.

#### POC - TestCaseFile

- 1. https://github.com/0xJoichiro/2024-02-rubicon-finance/blob/af571355747b41f5b7c672147e0c3401acd8270d/gladius-contracts-internal/test/reactors/GladiusReactor.t.sol#L755

---------------------------------------------------------


## Contest 303 - Beefy Cowcentrated Liquidity Manager

- https://audits.sherlock.xyz/contests/303
- https://github.com/0xJoichiro/2024-05-beefy-cowcentrated-liquidity-manager

<img src="image-4.png" alt="alt text" height="50%" width="50%">



### Valid - (1), Invalid 115

- 1. [M1 - Accounting will be broken if output token is one of the lpTokens](https://github.com/sherlock-audit/2024-05-beefy-cowcentrated-liquidity-manager-judging/issues/101)

#### Summary

- 1. `StrategyPassiveManagerVelodrome's` functionality would break when being initialized with a pool that has one of the trading tokens as a reward token.Accounting will be broken if output token is one of the lpTokens.The problem is that the output token might be one of the lpTokens too and any accrued fees that are not yet harvested will be included in this number.

#### POC - TestCaseFile

- 1. https://github.com/0xJoichiro/2024-05-beefy-cowcentrated-liquidity-manager/blob/main/cowcentrated-contracts/test/forge/POC.t.sol

`forge test --match-path test/forge/POC.t.sol --fork-url https://rpc.ankr.com/optimism --fork-block-number 120567055 -vv`


---------------------------------------------------------


## Contest 130 - DODO V3 update

- https://audits.sherlock.xyz/contests/130
- https://github.com/0xJoichiro/2023-12-dodo

<img src="image-5.png" alt="alt text" height="50%" width="50%">

### Valid - (1), Invalid 35

- 1. [M1- Inability to Re-add oldToken After Execution of D3MakerFreeSlot.setNewTokenAndReplace()](https://github.com/sherlock-audit/2023-12-dodo-judging/issues/19)

#### Summary

- 1. The setNewTokenAndReplace() function is designed to replace an existing token with a new token in a slot, thereby saving gas. However, this function only removes the oldToken's information from state.tokenMMInfoMap and does not clear its index from state.priceListInfo.tokenIndexMap. Consequently, the system behaves as if the oldToken is still present, preventing its re-addition.

#### POC - TestCaseFile

- 1. 



---------------------------------------------------------


## Contest 248 - xKeeper

- https://audits.sherlock.xyz/contests/248
- https://github.com/0xJoichiro/2023-12-dodo

<img src="image-6.png" alt="alt text" height="50%" width="50%">



### Valid - (2), Invalid 158

- 1. [M1 - Keep3r Relay Implementations are Not Compatible with Keep3r in Optimism and Executions Will Always Revert](https://github.com/sherlock-audit/2024-04-xkeeper-judging/issues/132)
- 2. [M2 - OpenRelay.sol does not account for the Layer1 gas fees used in the transaction while calculating the fee to be paid to the relayer](https://github.com/sherlock-audit/2024-04-xkeeper-judging/issues/32)

#### Summary

- 1. Keep3rRelay and Keep3rBondedRelay uses deprecated function for sidechains and exec calls will always revert.
- 2. The exec() function in OpenRelay.sol is structured in way that it calls the exec() function in AutomationVault.sol twice. First one with _execData where the jobs are specified and second one with the _feeData to be compensated for the job execution. While calculating the compensation amount after the first call it only includes the L2 gas fees (if the contracts are deployed on L2) and it does not include the L1 fees.

#### POC - TestCaseFile

- 1. 
- 2. 




<!-- ---------------------------------------------------------


## Contest Number - Name


<img src="image-7.png" alt="alt text" height="50%" width="50%">


### Valid - (1), Invalid 103

- 1. 

#### Summary

- 1. 

#### POC - TestCaseFile

- 1. 
 -->


# TBD

---------------------------------------------------------


## Contest 196 - Telcoin Platform Audit Update

<img src="image-7.png" alt="alt text" height="50%" width="50%">


### Valid - (2), Invalid 74

- 1. [M1 - BridgeRelay makes an approval to the same predicate address, despite different tokens/ eth having different predicates](https://github.com/sherlock-audit/2024-02-telcoin-platform-audit-update-judging/issues/40)
- 2. [M2 - Missing blacklist check beforeTokenTransfer allows anyone to bypass the blacklist mechanism](https://github.com/sherlock-audit/2024-02-telcoin-platform-audit-update-judging/issues/28)

#### Summary

- 1. When the BridgeRelay.transferERCToBridge gets called, it approves the hardcoded ERC20Predicate to use the ERC20 tokens. However, the bridge uses more than one predicate to lock the tokens. Here the bridge retrieves the predicate address based on the type of token to be bridged. If a token that uses different predicate than the hardcoded is sent to the BridgeRelay, it will be forever stuck there since the right predicate will not have approval to transfer it. There also exists a risk that a token can change its predicate at any time.
- 2. The stablecoin contracts inherit blacklisting mechanism. Although upon getting blacklisted, the user's funds are transferred, the user can still receive and send tokens, since non of the transferring methods are overridden.

#### POC - TestCaseFile

Command -> file link

- 1. npx hardhat test test/stablecoins/Stablecoin.test.ts -> https://github.com/0xJoichiro/2024-02-telcoin-platform-audit-update/blob/cfa0c4ec3d945cc643399353696e34286cd79eb3/telcoin-contracts/test/stablecoins/Stablecoin.test.ts#L93C1-L172C1
- 2. 


#### Giveaways

- hardcoded and key mapping for the same thing not checked
- Frontrun and backrun
- Transfer function wont care even if blacklisted
- EIP1967 storage slots
- Beacon proxy
- Oz ClonableBeaconProxy.sol
- ERC7201 
- 1967 eip
- 


---------------------------------------------------------


## Contest 330 - Gamma - Locked Staking Contract

- https://audits.sherlock.xyz/contests/330
- https://github.com/0xJoichiro/2024-05-gamma-staking



<img src="image-8.png" alt="alt text" height="50%" width="50%">


### Valid - (2), Invalid 298

- 1. 
- 2. 

#### Summary

- 1. 
- 2. 

#### POC - TestCaseFile

- 1. 
- 2. 


#### Giveaways


---------------------------------------------------------


## Contest 80 - Gamma - Locked Staking Contract

- https://audits.sherlock.xyz/contests/330
- https://github.com/0xJoichiro/2024-05-gamma-staking



<img src="image-8.png" alt="alt text" height="50%" width="50%">


### Valid - (2), Invalid 298

- 1. 
- 2. 

#### Summary

- 1. 
- 2. 

#### POC - TestCaseFile

- 1. 
- 2. 


#### Giveaways




  {
    "contest_id": "80",
    "scope": "553 nSLOC",
    "num_issues": 2,
    "nsloc_num": 553,
    "rating": 1106,
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
    "contest_id": "187",
    "scope": "1,083 nSLOC",
    "num_issues": 2,
    "nsloc_num": 1083,
    "rating": 2166,
    "status": "No"
  },
  {
    "contest_id": "281",
    "scope": "1,971 nSLOC",
    "num_issues": 2,
    "nsloc_num": 1971,
    "rating": 3942,
    "status": "No"
  },
  {
    "contest_id": "103",
    "scope": "2,760 nSLOC",
    "num_issues": 2,
    "nsloc_num": 2760,
    "rating": 5520,
    "status": "No"
  },