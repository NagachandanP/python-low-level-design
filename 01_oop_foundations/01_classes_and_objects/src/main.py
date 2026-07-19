from car import Car


def main() -> None:
    car = Car(
        brand="Toyota",
        model="Corolla",
        year=2024,
        color="White",
    )

    print("Initial State")
    car.display_information()

    print("\nAccelerating by 40 km/h...")
    car.accelerate(40)
    car.display_information()

    print("\nBraking by 15 km/h...")
    car.brake(15)
    car.display_information()

    print("\nStopping...")
    car.stop()
    car.display_information()


if __name__ == "__main__":
    main()