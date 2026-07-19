# Sequence Diagram - Borrow a Book

## Problem Statement

Illustrate the interaction between the objects involved when a member borrows a book.

---

```mermaid
sequenceDiagram

actor Member

participant Library
participant Book

Member->>Library: Search Book
Library-->>Member: Book Found

Member->>Library: Borrow Book

Library->>Book: Check Availability

Book-->>Library: Available

Library->>Book: Mark as Borrowed

Book-->>Library: Success

Library-->>Member: Book Issued
```

---

## Observation

This diagram focuses on the **runtime interaction** between objects.

It answers:

- Which object communicates first?
- What messages are exchanged?
- In what sequence do they occur?

Unlike a Class Diagram, it emphasizes **behavior over structure**.