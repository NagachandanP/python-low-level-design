# Use Case Diagram - Library Management System

## Problem Statement

Model the interactions between users and the Library Management System.

---

```mermaid
flowchart LR

Member((Member))
Librarian((Librarian))

Search([Search Book])
Borrow([Borrow Book])
Return([Return Book])

Add([Add Book])
Remove([Remove Book])
Update([Update Book])

Member --> Search
Member --> Borrow
Member --> Return

Librarian --> Add
Librarian --> Remove
Librarian --> Update
```

---

## Observation

This diagram answers **WHO** uses the system and **WHAT** they can do.

It does **not** describe:

- Internal classes
- Object interactions
- Execution order

Those will be covered by other UML diagrams.