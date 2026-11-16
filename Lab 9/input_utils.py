def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                raise ValueError("Value must be greater than zero.")

            return value

        except ValueError:
            print("Invalid input. Please enter a positive number.")