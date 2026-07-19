"""
Unit tests for the Car class.
"""

import unittest

from src.car import Car


class TestCar(unittest.TestCase):
    """Test cases for the Car class."""

    def test_constructor_initializes_attributes(self) -> None:
        """Verify that the constructor initializes all attributes."""

        car = Car(
            brand="Toyota",
            model="Corolla",
            year=2024,
            color="White",
        )

        self.assertEqual(car.brand, "Toyota")
        self.assertEqual(car.model, "Corolla")
        self.assertEqual(car.year, 2024)
        self.assertEqual(car.color, "White")
        self.assertEqual(car.current_speed, 0)

    def test_accelerate(self) -> None:
        """Verify accelerate increases speed."""

        car = Car("Toyota", "Corolla", 2024, "White")

        car.accelerate(40)

        self.assertEqual(car.current_speed, 40)

    def test_brake(self) -> None:
        """Verify brake decreases speed."""

        car = Car("Toyota", "Corolla", 2024, "White")

        car.accelerate(50)
        car.brake(20)

        self.assertEqual(car.current_speed, 30)

    def test_stop(self) -> None:
        """Verify stop resets speed."""

        car = Car("Toyota", "Corolla", 2024, "White")

        car.accelerate(90)
        car.stop()

        self.assertEqual(car.current_speed, 0)


if __name__ == "__main__":
    unittest.main()