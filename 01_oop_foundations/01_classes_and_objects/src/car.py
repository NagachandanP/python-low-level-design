"""
Lesson 1: Classes and Objects

This module defines the Car class used to demonstrate
basic Object-Oriented Programming concepts.
"""


class Car:
    """Represents a car."""

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        color: str,
    ) -> None:
        """
        Initialize a new Car object.

        Args:
            brand: Manufacturer of the car.
            model: Model name.
            year: Manufacturing year.
            color: Exterior color.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.current_speed = 0


    def __repr__(self) -> str:
        """Return a developer-friendly string representation of the Car."""

        return (
            f"Car("
            f"brand='{self.brand}', "
            f"model='{self.model}', "
            f"year={self.year}, "
            f"color='{self.color}', "
            f"current_speed={self.current_speed}"
            f")"
        )
    
    def accelerate(self, speed: int) -> None:
        """Increase the current speed."""
        self.current_speed += speed


    def brake(self, speed: int) -> None:
        """Decrease the current speed without going below zero."""
        self.current_speed = max(0, self.current_speed - speed)


    def stop(self) -> None:
        """Stop the car."""
        self.current_speed = 0


    def display_information(self) -> None:
        """Display the car's information."""
        print(f"Brand         : {self.brand}")
        print(f"Model         : {self.model}")
        print(f"Year          : {self.year}")
        print(f"Color         : {self.color}")
        print(f"Current Speed : {self.current_speed} km/h")