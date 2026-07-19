# Activity Diagram - Borrow a Book

## Problem Statement

Illustrate the business workflow for borrowing a book.

---

```mermaid
flowchart TD

Start([Start])

Search[Search Book]

Available{Book Available?}

Borrow[Borrow Book]

Update[Update Book Status]

Success[Book Issued]

Failure[Notify Member]

End([End])

Start --> Search

Search --> Available

Available -- Yes --> Borrow

Borrow --> Update

Update --> Success

Success --> End

Available -- No --> Failure

Failure --> End
```

---

## Observation

This diagram models the **business process**, not the software objects.

It answers:

- What steps are involved?
- What decisions are made?
- What are the possible outcomes?