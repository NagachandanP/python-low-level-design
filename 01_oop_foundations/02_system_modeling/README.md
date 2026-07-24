# Lesson 02 — UML System Modeling

> **Module:** OOP Foundations
> **Status:** ✅ Completed
> **Difficulty:** Beginner
> **Current Version:** V4

---

# Problem Statement

Before writing software, engineers first design the system.

Writing code without understanding the system often leads to poor architecture, duplicated logic, and unnecessary refactoring.

In this lesson, we model a simple **Online Shopping System** using UML diagrams.

The goal is to understand the system from multiple perspectives before implementing it in Python.

---

# Learning Objectives

By the end of this lesson, you will be able to:

- Understand why UML is used.
- Identify actors from requirements.
- Identify candidate classes.
- Understand object interactions.
- Model business workflows.
- Draw UML diagrams using Mermaid.
- Explain UML diagrams during interviews.

---

# Version Evolution

| Version | Evolution |
|----------|-----------|
| V1 | Requirement Analysis |
| V2 | Use Case Diagram |
| V3 | Class Diagram |
| V4 | Sequence & Activity Diagrams |

---

# Folder Structure

```text
02_system_modeling/

├── docs/
│   ├── use_case_diagram.md
│   ├── class_diagram.md
│   ├── sequence_diagram.md
│   └── activity_diagram.md
│
├── examples/
│
├── NOTES.md
└── README.md
```

---

# Why UML?

UML (Unified Modeling Language) helps software engineers visualize and communicate system designs before implementation.

Instead of immediately writing code, we first answer important design questions.

---

# Diagram Selection Guide

| Question | Diagram |
|-----------|----------|
| Who uses the system? | Use Case Diagram |
| What classes exist? | Class Diagram |
| How do objects communicate? | Sequence Diagram |
| How does the business process flow? | Activity Diagram |

---

# Design Process

```text
Requirements
      ↓
Identify Actors
      ↓
Identify Classes
      ↓
Identify Relationships
      ↓
Identify Interactions
      ↓
Draw UML
      ↓
Start Coding
```

---

# How to View the Diagrams

GitHub automatically renders Mermaid diagrams.

Simply open the corresponding Markdown file inside the **docs** folder.

---

# Current Limitations

The diagrams intentionally model only a small portion of an Online Shopping System.

Advanced concepts like:

- Payment
- Inventory
- Shipping
- Coupons
- Authentication

will be introduced in later projects.

---

# Future Improvements

Later projects will include:

- Multiplicity
- Composition
- Aggregation
- Inheritance
- Interfaces
- Design Patterns
- Microservice boundaries

---

# Interview Corner

## 🟢 Basic

### What is UML?

**Answer**

UML (Unified Modeling Language) is a standard visual language used to model software systems before implementation.

---

### Why is UML used?

**Answer**

UML helps developers visualize, discuss, and validate system designs before writing code.

---

## 🟡 Intermediate

### Difference between Class Diagram and Sequence Diagram?

**Answer**

A Class Diagram shows the static structure of the system.

A Sequence Diagram shows how objects communicate during runtime.

---

### Why should software be designed before coding?

**Answer**

Designing first helps identify missing requirements, improves architecture, reduces future refactoring, and allows teams to communicate effectively.

---

## 🔴 Advanced

### Which UML diagrams are most useful for Low-Level Design interviews?

**Answer**

The four most commonly used diagrams are:

- Use Case Diagram
- Class Diagram
- Sequence Diagram
- Activity Diagram

These are sufficient for explaining most interview problems.

---

# Lesson Summary

## What We Built

Using a simple **Online Shopping System**, we created:

- Use Case Diagram
- Class Diagram
- Sequence Diagram
- Activity Diagram

---

## Concepts Mastered

- UML
- Actors
- Classes
- Relationships
- Runtime Interaction
- Business Workflow

---

## Key Takeaways

- UML should be created before implementation.
- Every UML diagram answers a different design question.
- Modeling first improves software quality.
- Mermaid makes UML documentation GitHub-friendly.

---

# Next Lesson

## Lesson 03 — Encapsulation

Example:

**Bank Account**

Topics:

- Public vs Private Members
- Name Mangling
- Getter & Setter
- @property
- Validation
- Protecting Object State