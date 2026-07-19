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

# Interview Corner

## 🟢 Basic Questions

### 1. What is a Class?

**Answer:**

A class is a blueprint or template used to create objects. It defines the attributes (state) and methods (behavior) that every object created from it will have.

**Example**

```python
class Car:
    pass
```

---

### 2. What is an Object?

**Answer:**

An object is an instance of a class. Each object has its own independent state while sharing the behavior defined by the class.

**Example**

```python
car1 = Car("Toyota", "Corolla", 2024, "White")
car2 = Car("Honda", "City", 2023, "Black")
```

Although both are `Car` objects, they maintain different data.

---

### 3. What is the purpose of `self`?

**Answer:**

`self` refers to the current object instance. It allows methods to access and modify that object's attributes and call its other methods.

Without `self`, Python would not know which object's data should be accessed.

---

### 4. What is the purpose of `__init__()`?

**Answer:**

`__init__()` is the constructor of a class. It is automatically called when an object is created and is responsible for initializing the object's state.

---

### 5. What is the purpose of `__repr__()`?

**Answer:**

`__repr__()` returns a developer-friendly representation of an object. It is mainly used for debugging and logging.

Instead of displaying:

```text
<__main__.Car object at 0x000001F8A23B4D90>
```

it displays:

```text
Car(brand='Toyota', model='Corolla', year=2024, color='White', current_speed=0)
```

---

## 🟡 Intermediate Questions

### 6. What is the difference between State and Behavior?

**Answer:**

**State** represents the data stored inside an object.

Example:

- brand
- model
- year
- current_speed

**Behavior** represents the actions an object can perform.

Example:

- accelerate()
- brake()
- stop()

A well-designed object combines both state and behavior.

---

### 7. Why should behavior be inside the class?

**Answer:**

Keeping behavior inside the class follows the principles of Object-Oriented Programming by keeping data and the operations on that data together.

Instead of:

```python
speed += 20
```

we write:

```python
car.accelerate(20)
```

This improves readability, maintainability, and encapsulation.

---

### 8. Why does every new Car start with `current_speed = 0`?

**Answer:**

This is a design decision. A newly created car should begin in a valid initial state. The constructor ensures every object starts consistently.

---

## 🔴 Advanced Questions

### 9. Is the current implementation production-ready?

**Answer:**

No.

The class currently allows invalid inputs, for example:

```python
car.accelerate(-50)
```

or

```python
Car("", "", -1, "")
```

There is no validation yet.

This is intentional because future lessons will introduce encapsulation, validation, and SOLID principles to improve the design incrementally.

---

### 10. How would you improve this class?

**Answer:**

Some possible improvements include:

- Encapsulate attributes using `@property`
- Validate constructor inputs
- Prevent negative speed
- Raise meaningful exceptions for invalid operations
- Add more unit tests covering edge cases
- Refactor the design using SOLID principles

---

### 11. Why are unit tests important?

**Answer:**

Unit tests verify that each unit of code behaves as expected.

Benefits include:

- Detect regressions after code changes
- Increase confidence during refactoring
- Document expected behavior
- Improve software quality

---

# Key Takeaways

- A class is a blueprint.
- An object is an instance of a class.
- Objects contain both state and behavior.
- Constructors initialize object state.
- `__repr__()` improves debugging.
- Unit tests verify expected behavior.

---

# Lesson Summary

## 📌 What We Built

In this lesson, we designed and implemented our first object-oriented model using a `Car` class.

The implementation includes:

- A `Car` class with state and behavior
- Constructor (`__init__`)
- `__repr__()` for object representation
- Business methods (`accelerate`, `brake`, `stop`, `display_information`)
- Unit tests using Python's `unittest`
- UML Class Diagram using Mermaid
- Documentation and personal notes

---

## 📚 Concepts Mastered

- Classes
- Objects
- Instances
- Constructors (`__init__`)
- `self`
- Instance Variables
- State vs Behavior
- Object Representation (`__repr__`)
- Basic Unit Testing
- UML Class Diagram

---

## 🏗 Design Evolution

```
Version 1 → Empty Car class
        ↓
Version 2 → Added constructor
        ↓
Version 3 → Added __repr__()
        ↓
Version 4 → Added object behavior
        ↓
Version 5 → Added unit tests
        ↓
Version 6 → Added UML & Documentation
```

---

## 🎯 Key Takeaways

- A class acts as a blueprint for creating objects.
- Every object maintains its own independent state.
- Methods define the behavior of an object.
- Constructors ensure objects start in a valid initial state.
- Testing verifies correctness and protects against regressions.
- UML diagrams communicate the design before and alongside implementation.

---

## 🚀 Ready for the Next Lesson?

✅ Yes

**Next Lesson:** `02_system_modeling`

In the next lesson, we'll learn how to think like a software designer by creating:

- Class Diagrams
- Sequence Diagrams
- Use Case Diagrams

before writing production code.