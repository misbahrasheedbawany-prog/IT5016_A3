# Simple Calculator Program
# This program demonstrates basic software design principles.


# Modularity:
# This function has one responsibility: adding two numbers.
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


# Modularity:
# This function has one responsibility: subtracting two numbers.
def subtract_numbers(a, b):
    """Return the difference between two numbers."""
    return a - b


# Modularity:
# This function has one responsibility: multiplying two numbers.
def multiply_numbers(a, b):
    """Return the product of two numbers."""
    return a * b


# Error Handling:
# This function checks for division by zero before calculating.
def divide_numbers(a, b):
    """Return the division result."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Separation of Responsibilities:
# The main function controls the program and calls the other functions.
def main():
    """Run the calculator program."""

    number1 = 10
    number2 = 5

    print("Addition:", add_numbers(number1, number2))
    print("Subtraction:", subtract_numbers(number1, number2))
    print("Multiplication:", multiply_numbers(number1, number2))
    print("Division:", divide_numbers(number1, number2))


# This starts the program when the file is run directly.
if __name__ == "__main__":
    main()
