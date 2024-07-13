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


<!-- ---------------------------------------------------------


## Contest Number - Name


image


### Valid - (1), Invalid 103

- 1. 

#### Summary

- 1. 

#### POC - TestCaseFile

- 1. 
 -->




<!-- 
- 
- 130 -->