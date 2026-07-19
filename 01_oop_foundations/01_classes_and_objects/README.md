# Lesson 01 — Classes and Objects

> **Module:** OOP Foundations  
> **Status:** ✅ Completed  
> **Difficulty:** Beginner  
> **Current Version:** V5

---

# Problem Statement

Before designing large systems such as a Parking Lot, Library Management System, or ATM, we must first learn how to model a single real-world entity.

In this lesson, we model a **Car** as an object by identifying:

- What information it stores (**State**)
- What actions it can perform (**Behavior**)

This is the foundation of Object-Oriented Programming (OOP).

---

# Learning Objectives

By the end of this lesson, you will understand:

- What is a Class?
- What is an Object?
- What is an Instance?
- How constructors (`__init__`) work
- Why `self` is required
- Instance Variables
- Object State
- Object Behavior
- The purpose of `__repr__()`
- Writing basic Unit Tests using `unittest`

---

# Evolution

Software is built incrementally. Instead of writing the perfect solution immediately, this lesson evolves the `Car` class step by step.

| Version | Evolution |
|----------|-----------|
| V1 | Created an empty `Car` class |
| V2 | Added constructor and initialized object state |
| V3 | Added `__repr__()` for better debugging |
| V4 | Added object behaviors (`accelerate`, `brake`, `stop`, `display_information`) |
| V5 | Added unit tests |

---

# Folder Structure

```text
01_classes_and_objects/

├── docs/
│   └── class_diagram.md
│
├── src/
│   ├── car.py
│   └── main.py
│
├── tests/
│   └── test_car.py
│
├── NOTES.md
└── README.md
```

---

# Implementation Overview

The `Car` class models a real-world car.

## State

- brand
- model
- year
- color
- current_speed

## Behavior

- accelerate()
- brake()
- stop()
- display_information()

---

# Design Decisions

### Why does every new Car start with speed = 0?

A newly created car should begin in a valid state.

This is a **business decision**, not a Python language requirement.

---

### Why is behavior inside the class?

Instead of modifying variables directly,

```python
speed += 20
```

we encapsulate behavior inside the object.

```python
car.accelerate(20)
```

This makes the design easier to understand and maintain.

---

### Why implement `__repr__()`?

The default Python object representation only displays the memory address.

Implementing `__repr__()` provides a meaningful representation that greatly improves debugging.

---

# How to Run

```bash
cd src
python main.py
```

---

# How to Run Tests

From the lesson directory:

```bash
python -m unittest discover tests
```

Expected output:

```text
....
----------------------------------------------------------------------
Ran 4 tests

OK
```

---

# UML

The UML Class Diagram is available here:

```
docs/class_diagram.md
```

---

# Current Limitations

This implementation is intentionally simple.

The following improvements will be introduced in future lessons:

- Attribute validation
- Encapsulation using `@property`
- Preventing invalid state
- Better error handling
- More comprehensive unit tests

---

# Interview Questions

- What is a Class?
- What is an Object?
- What is an Instance?
- What is the purpose of `self`?
- What is `__init__()`?
- What is the difference between State and Behavior?
- Why should methods belong inside the class?
- What is `__repr__()`?
- Why are unit tests important?

---

# Key Takeaways

- A class is a blueprint.
- An object is an instance of a class.
- Objects contain both state and behavior.
- Constructors initialize object state.
- `__repr__()` improves debugging.
- Unit tests verify expected behavior.

---

# Next Lesson

**Lesson 02 — System Modeling**

We'll learn how to represent software designs visually using UML diagrams, including:

- Class Diagrams
- Sequence Diagrams
- Use Case Diagrams

Before writing code, we should first learn how to design the system.