# Sequence Diagram - Place Order

## Problem Statement

Illustrate the interaction between objects when a customer places an order.

Unlike the Class Diagram, this diagram focuses on **runtime communication**.

---

## Mermaid UML

```mermaid
sequenceDiagram

actor Customer

participant ShoppingSystem
participant Product

Customer->>ShoppingSystem: Search Product

ShoppingSystem-->>Customer: Product Found

Customer->>ShoppingSystem: Place Order

ShoppingSystem->>Product: Check Stock

Product-->>ShoppingSystem: In Stock

ShoppingSystem->>Product: Reduce Stock

Product-->>ShoppingSystem: Stock Updated

ShoppingSystem-->>Customer: Order Confirmed
```

---

# Observation

This diagram answers:

- Which object starts the interaction?
- Which object communicates next?
- What messages are exchanged?
- In what order do they occur?

---

# Key Takeaways

- Sequence Diagrams represent runtime behavior.
- Time flows from top to bottom.
- Horizontal arrows represent messages exchanged between objects.
- They are excellent for explaining workflows during interviews.