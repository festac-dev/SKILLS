# NEAR and Cross-Chain Engineering Specialist

## When to use
Load for NEAR contracts/accounts, asynchronous receipts, intents, bridges, relayers, account abstraction, or cross-chain settlement.

## Core principles
Do not model cross-chain work as one atomic transaction. Separate source acceptance, finality, message verification, destination execution, and economic settlement. A bridge or intent solver introduces a trust and liveness model.

## Step-by-step procedure
1. Identify each chain, account/key model, finality policy, relayer/solver, fees, refunds, and trust assumptions.
2. On NEAR, distinguish transaction acceptance from downstream receipt outcomes. Validate callback predecessor/origin as appropriate; handle failed promises and storage deposits.
3. Restrict function-call keys and contract permissions to intended methods/allowances. Review account-abstraction validation and replay protection rather than assuming one wallet equals one private key.
4. Bind cross-chain messages to source chain, destination chain, contract, nonce, payload, and expiry. Verify proof/signature and finality under the bridge model.
5. Define pending, executed, failed, refunded, and disputed states. Make delivery and settlement idempotent.
6. Test delayed/duplicate/reordered messages, expired intents, unavailable solvers, reorgs, partial execution, and refund recovery on local/test environments.

## Checklist
- [ ] Assets cannot be minted/released twice from a replay.
- [ ] A source success does not falsely imply destination success.
- [ ] Fee/storage refunds and abandoned work have owners.
- [ ] Mainnet keys and destinations require explicit scope.

## Common failure modes
Ignoring asynchronous failure; trusting a relayer without verification; missing chain-domain separation; assuming bridge security equals base-chain security; intents execute outside user slippage/expiry bounds.

## Concrete examples
NEAR CLI implementations differ: run `near --version` and `near --help`, then verify against current docs for that installed CLI before selecting commands. A replay test submits the same synthetic message ID twice and asserts one settlement, one recorded duplicate, and unchanged total assets.

## Verification
Record network, CLI/SDK version, receipt chain, replay cases, asset reconciliation, trust assumptions, and recovery results.

## Related skills
[EVM](evm-transaction-engineering.md), [distributed workflows](edge-and-distributed-systems.md), [ledger systems](fintech-and-ledger-systems.md).

## Applied verification

Delay a downstream receipt after source acceptance, then redeliver the message. Assert one destination effect or the specified refund and a truthful pending state; verify contract, chain and nonce domain separation.
