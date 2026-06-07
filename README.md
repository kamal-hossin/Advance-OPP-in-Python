# Python OOP Examples

This repository contains simple Python examples to demonstrate advanced Object-Oriented Programming (OOP) concepts.

## Files and Concepts

- `composition.py`
  - Demonstrates composition, where a `Car` object contains an `Engine` object.
  - Shows "HAS-A" relationship and how one object can use another to perform work.

- `decorator.py`
  - Demonstrates Python property decorators.
  - Includes a getter using `@property`, a setter using `@balance.setter`, and a read-only property.
  - Shows how to encapsulate access to internal attributes.

- `getter_setter_readonly.py`
  - Demonstrates explicit getter and setter methods for private attributes.
  - Uses a read-only property via `@property`.
  - Shows how to protect and control direct access to object state.

- `overloading.py`
  - Demonstrates method overloading-like behavior using default arguments.
  - Includes a base class `Person` and a subclass `Cricket_Player`.
  - Shows an overridden method that also accepts optional arguments.

- `override.py`
  - Demonstrates method overriding in subclassing.
  - `Cricket_Player` overrides the base `Person` method to provide specialized behavior.

- `static.py`
  - Demonstrates static and class methods.
  - Includes a static attribute `school`, a static method `greet()`, and a class method `change_school()`.
  - Shows how class-level behavior differs from instance-level behavior.

## How to Run

Run each file individually with Python. For example:

```bash
python composition.py
python decorator.py
python getter_setter_readonly.py
python overloading.py
python override.py
python static.py
```

## Notes

- These examples are intentionally simple for learning and demonstration.
- They illustrate core Python OOP patterns commonly used in real code.
