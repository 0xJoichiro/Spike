## Notes
![alt text](image.png)


### EIP


### EIP-712

- EIP-712 standard describes how data is structured, hashed, and signed. Signing a transaction has been around in crypto wallets like Metamask, but this approach aims to display that in a much more human-readable way that users can understand and review before signing.


#### EIP-2771 

- OpenZepplin provides a utility contract called ERC2771Context to make it easy for the smart contract developer to extract the intended msg.sender and msg.data out of the data sent by the MinimalForwarder.


#### EIP-4626

#### EIP-7540



#### ERC1404



### Delegatecall

- When contract A executes delegatecall to contract B, B's code is executed with contract A's storage, msg.sender and msg.value.
- In Solidity, delegatecall is a low-level function that allows a contract to delegate its call to another contract (borrowing the functionality of another contract) while still preserving its own storage and context. When a contract makes a delegatecall, the code at the target address is executed in the context of the calling contract. This means that the storage, state variables, and functions of the calling contract are accessible to the code being executed.
- https://medium.com/@ajaotosinserah/mastering-delegatecall-in-solidity-a-comprehensive-guide-with-evm-walkthrough-6ddf027175c7
- https://medium.com/@bansaltushar014/delegatecall-in-solidity-4138b121cbe
- 

### Clones from OZ


### Proxy systems


### aave flashloan callback and initiator


### Weird ERC20



### Slippage protection

### Sandwich attack


### L1 to L2 fees

- The Gelato protocol properly handles L1 data fees(https://docs.gelato.network/web3-services/relay/gelatos-fee-oracle#arguments-2)
- Every L2 has its own formula for calculating the L1 data fee, so different versions of the code will have to be written for each L2
- There are two types of gas fees on L2s: The L2 execution fees and the L1 Data fees.


### EIP1559 gas algorithm