# EVM Transaction Engineering Specialist

## When to use
Load for wallet integration, signing, gas, nonce handling, EVM RPC, chain selection, or transaction tracking. Contract implementation belongs to the Solidity specialist.

## Core principles
Default experiments to local chains or testnets with disposable keys. Chain ID, destination, calldata, value, fee policy, and signer must be visible and verified before signing. Never infer mainnet authorization from testnet work.

## Step-by-step procedure
1. Identify chain/network, RPC trust, account type, wallet provider, supported transaction types, and confirmation/finality requirements.
2. Keep private keys in approved signing systems; never request seed phrases in chat or place keys in command history.
3. Validate address/network, token decimals, amounts, nonce ownership, fee ceiling, and spending allowance. Avoid unlimited approvals by default.
4. Simulate or estimate with the intended sender and state where supported. Simulation is not a guarantee against state changes or MEV.
5. Obtain authorization for the concrete signing/broadcast action when required. Record transaction hash and distinguish submitted, pending, included, confirmed, replaced, reverted, and reorged.
6. Reconcile on-chain state after timeouts before rebroadcasting. Handle replacement transactions and nonce collisions explicitly.

## Checklist
- [ ] Testnet/mainnet state is clearly separated.
- [ ] Fees, spender, allowance, value, and chain are bounded.
- [ ] Signatures include the correct domain and replay protections.
- [ ] No receipt is treated as final without the network-specific policy.

## Common failure modes
Wrong-chain signing; decimal conversion errors; blind message signatures; unlimited approvals; timeout-triggered duplicate economic effects; treating an RPC response as consensus truth.

## Concrete examples
With Foundry installed, inspect `cast --version`, `cast chain-id --help`, and `cast call --help`. Read-only local network identification: `cast chain-id --rpc-url http://127.0.0.1:8545`. Never substitute a production endpoint and signer without reviewing the action scope.

## Verification
Test failed simulation, rejected signature, reverted transaction, replacement, nonce conflict, RPC outage, and reorg handling in a disposable environment. Record chain ID and transaction evidence without key material.

## Related skills
[Solidity](solidity-contract-engineering.md), [cross-chain](near-and-cross-chain-engineering.md), [financial correctness](fintech-and-ledger-systems.md).

## Applied verification

Exercise rejection, replacement and reorg handling on the authorized test network. Bind the displayed outcome to chain, sender, nonce and receipt status; submitting a transaction hash does not prove final settlement.
