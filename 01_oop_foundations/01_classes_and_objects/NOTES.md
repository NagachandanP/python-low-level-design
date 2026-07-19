# Lesson Notes - Classes and Objects

## Key Concepts

### Class
A class is a blueprint used to create objects.

### Object
An object is an instance of a class with its own state and behavior.

### State
State represents the data stored inside an object.

Example:
- brand
- model
- year
- color
- current_speed

### Behavior
Behavior represents the actions an object can perform.

Example:
- accelerate()
- brake()
- stop()
- display_information()

### Constructor (`__init__`)
The constructor initializes the object's state when it is created.

### self
`self` refers to the current object instance and allows access to its attributes and methods.

### `__repr__()`
Provides a developer-friendly string representation of an object, making debugging easier.

---

# What I Learned

- Every object has its own independent state.
- Methods operate on the object's own state.
- Constructors ensure objects start in a valid initial state.
- Unit tests verify that object behavior works as expected.
- UML diagrams help visualize the design before or alongside implementation.

---

# Common Mistakes

- Forgetting to use `self`.
- Creating objects without required constructor arguments.
- Putting business logic outside the class.
- Assuming every object shares the same state.

---

# Future Improvements

In upcoming lessons, this `Car` class will be improved by:

- Encapsulation using `@property`
- Input validation
- Better error handling
- Applying SOLID principles
- Refactoring with design patterns