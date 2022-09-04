from typing import Optional


class Person:
  # Providing a parameterized constructor
  # Optional[..] is like Nullable<> or ?
  # None is basically null or nil
  def __init__(self, name: str, age: Optional[int] = None) -> None:
    self.name = name
    self.age = age

  # Overriding the toString
  def __str__(self) -> str:
    # Using python's string interpolation
    return f'Person(name={self.name},age={self.age})'