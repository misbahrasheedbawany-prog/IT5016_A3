# Simple Calculator Program
# This program demonstrates basic software design principles
# such as modularity, readability, and separation of responsibilities.


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract_numbers(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b


def divide_numbers(a, b):
    """Return the division result."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b


def main():
    """Run the calculator program."""

    number1 = 10
    number2 = 5

    print("Addition:", add_numbers(number1, number2))
    print("Subtraction:", subtract_numbers(number1, number2))
    print("Multiplication:", multiply_numbers(number1, number2))
    print("Division:", divide_numbers(number1, number2))


if __name__ == "__main__":
    main()
