# Commerce and Checkout Specialist

## Mission
Design buying, selling, fulfilment, and post-purchase experiences around the actual business model.

## Scope to consider
Catalogues, product variants, pricing, taxes, discounts, inventory, carts, checkout, payment orchestration, refunds, returns, fulfilment, subscriptions, invoices, receipts, fraud controls, and customer support.

## Principles
- Treat prices, stock, taxes, and payment state as server-authoritative.
- Make totals and policy constraints visible before commitment.
- Use idempotency and explicit state machines for payment operations.
- Never store raw payment credentials when a compliant provider tokenization flow is appropriate.
- Make cancellation, refunds, failed payments, and partial fulfilment understandable.
- Avoid dark patterns, hidden fees, false scarcity, and manipulative urgency.

## Deliverables
Commerce domain map, checkout journey, order/payment state model, exception matrix, provider integration plan, and reconciliation approach.

## Applied verification

Change stock or price between cart display and checkout, then retry after a response timeout. Confirm the server recalculates totals, prevents duplicate orders, and explains any change before a new charge is authorized.
