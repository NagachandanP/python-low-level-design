# Lesson 02 — System Modeling

> **Module:** OOP Foundations  
> **Status:** ✅ Completed  
> **Difficulty:** Beginner  
> **Current Version:** V4

---

# Problem Statement

Before writing code, software engineers first model the system.

System modeling helps us understand:

- Who uses the system?
- What objects exist?
- How objects communicate?
- How the business workflow proceeds?

In this lesson, we model a simple **Library Management System** using UML.

---

# Learning Objectives

After completing this lesson, you will be able to:

- Understand why UML is used.
- Differentiate between the four most important UML diagrams.
- Draw UML using Mermaid.
- Convert requirements into software models.
- Prepare UML diagrams commonly discussed in LLD interviews.

---

# Evolution

| Version | Evolution |
|----------|-----------|
| V1 | Identified system requirements |
| V2 | Created Use Case Diagram |
| V3 | Created Class Diagram |
| V4 | Created Sequence & Activity Diagrams |

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

# Diagram Selection Guide

| If you want to know... | Use |
|-------------------------|-----|
| Who uses the system? | Use Case Diagram |
| What classes exist? | Class Diagram |
| How objects interact? | Sequence Diagram |
| How the workflow proceeds? | Activity Diagram |

---

# Design Process

```
Requirements
      ↓
Identify Actors
      ↓
Identify Classes
      ↓
Identify Relationships
      ↓
Model Interactions
      ↓
Draw UML
```

---

# Key Takeaways

- UML helps visualize software before implementation.
- Different UML diagrams answer different design questions.
- Modeling first reduces design mistakes during implementation.
- Mermaid allows UML diagrams to render directly on GitHub.

---

# Interview Corner

## 🟢 Basic

### What is UML?

**Answer:** UML (Unified Modeling Language) is a standard visual language used to model software systems before implementation.

---

### Why do we create UML diagrams?

**Answer:** To communicate the design clearly, identify potential issues early, and establish a common understanding before writing code.

---

## 🟡 Intermediate

### Difference between Class Diagram and Sequence Diagram?

**Answer:**

- Class Diagram → Static structure (classes and relationships)
- Sequence Diagram → Runtime interaction (message flow)

---

### Why not start coding immediately?

**Answer:**

Designing first helps identify missing requirements, improve architecture, and reduce costly refactoring later.

---

## 🔴 Advanced

### Which UML diagrams are most useful in Low-Level Design interviews?

**Answer:**

- Use Case Diagram
- Class Diagram
- Sequence Diagram
- Activity Diagram

These diagrams are sufficient for explaining most LLD interview problems.

---

# Lesson Summary

## What We Built

- Use Case Diagram
- Class Diagram
- Sequence Diagram
- Activity Diagram

using Mermaid.js.

## Concepts Mastered

- UML
- Actors
- Classes
- Relationships
- Object Interaction
- Business Workflow

---

## Next Lesson

**Lesson 03 — Encapsulation**

We'll improve our `Car` class by:

- Making attributes private
- Using `@property`
- Adding validation
- Preventing invalid object state