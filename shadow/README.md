# Shadow Audits

![tumblr_316e10c8d40b715bb74303410499ec12_6a5ae5fe_1280](https://github.com/0xJoichiro/Spike/assets/119509722/945d3253-d47a-4259-819c-fdd5738a6520)

## https://github.com/code-423n4/2022-01-sandclock/tree/main

###



## https://github.com/code-423n4/2021-05-88mph/tree/main





## 178 in Auditbook


- https://github.com/code-423n4/2023-09-centrifuge/tree/main
- https://code4rena.com/audits/2023-09-centrifuge


- [x] Docs Read
- [ ] Code Read
  - Take notes inline 
- Report Read
  - examine bot reports
  - Auditbook Report
  - Take notes
- Test Read/Make
- Take notes


Automated findings output for the audit can be found [here](https://github.com/code-423n4/2023-09-centrifuge/blob/main/bot-report.md) within 24 hours of audit opening.

![alt text](assets/image.png)
![alt text](assets/image-1.png)
![alt text](assets/image2.png)
### Notes


src/util/Context.sol	6 =>
  meta txn info getter,Provides information about the current execution context, including the sender of the transaction and its data,msg.sender,msg.data

src/Escrow.sol	17 =>
  for keeping approval of token transfer, The logic flow of the contract is straightforward: an authorized ward calls the approve function, providing the necessary arguments. The function then approves the specified amount of tokens for transfer to the specified spender address and emits an event to notify other parties of this approval.

src/util/SafeTransferLib.sol	17 =>
  The code in SafeTransferLib.sol provides a standardized and secure way to interact with ERC20 tokens within other smart contracts. It abstracts away the low-level details of encoding and executing token operations, while also handling potential failures and reverting the transaction if any issues occur. This library can be imported and used by other smart contracts to simplify and secure their token-related operations.

src/util/Auth.sol	18 => The code does not perform any complex data transformations. It simply updates the wards mapping based on the provided user address and the caller's permissions.

src/admins/DelayedAdmin.sol	24 => The DelayedAdmin contract is designed to provide administrative control over a Root contract. It allows authorized users, known as wards, to perform certain actions on the Root contract, such as pausing, unpausing, scheduling new addresses to be relied upon (relys), and canceling scheduled relys.



src/UserEscrow.sol	30 => The UserEscrow contract is an escrow system that holds tokens for specific destinations. Its purpose is to ensure that once tokens are transferred into the contract, they can only be transferred out to pre-chosen destinations, and only by authorized administrators (called wards).destinations mapping.




src/admins/PauseAdmin.sol	30 => The important logic flow in this contract revolves around the management of pausers and the ability to pause the Root contract. Only authorized wards can add or remove pausers, and only authorized pausers can call the pause() function to halt the Root contract's operations.


src/token/RestrictionManager.sol	49 => The RestrictionManager.sol contract is an implementation of the ERC1404 standard, which is a set of rules for managing transfer restrictions in Ethereum-based tokens. The purpose of this contract is to enforce transfer restrictions based on whether the recipient address is a member or not.Overall, the RestrictionManager.sol contract acts as a gatekeeper for token transfers, ensuring that transfers are only allowed to addresses that are currently members according to the members mapping.


src/Root.sol	66 => The Root.sol contract is a core contract that acts as a ward (a privileged role) on all other deployed contracts. Its primary purpose is to provide a mechanism for managing and controlling access to other contracts in the system.


src/token/Tranche.sol	76 => The TrancheToken contract is an extension of the ERC20 token standard and implements the ERC1404Like interface. Its purpose is to manage liquidity pools and enforce transfer restrictions for a specific type of token called a "tranche token."


src/gateway/routers/axelar/Router.sol	88 => The AxelarRouter contract is a Solidity smart contract that acts as a routing mechanism for integrating with an Axelar Gateway. Its purpose is to facilitate communication between different blockchain networks using the Axelar protocol.


src/util/Factory.sol	93 => 
src/token/ERC20.sol	183 => 
src/LiquidityPool.sol	225 => 
src/PoolManager.sol	261 => 
src/gateway/Gateway.sol	328 => 
src/InvestmentManager.sol	527 => 
src/gateway/Messages.sol	619 => 
```