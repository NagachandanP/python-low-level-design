# Class Diagram - Library Management System

## Problem Statement

Identify the core objects (classes) involved in a simple Library Management System and show how they are related.

---

```mermaid
classDiagram

class Member {
    +member_id
    +name
    +borrow_book()
    +return_book()
}

class Book {
    +book_id
    +title
    +author
    +is_available
}

class Librarian {
    +employee_id
    +name
    +add_book()
    +remove_book()
    +update_book()
}

class Library {
    +books
    +members
    +search_book()
}

Member --> Book : borrows
Librarian --> Library : manages
Library --> Book : contains
```

---

## Observation

This diagram answers:

- What are the important classes?
- What responsibilities do they have?
- How are they related?

It does **not** show the order in which methods are called.