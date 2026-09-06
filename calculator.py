# Simple Python Calculator
# A beginner-friendly command-line calculator

def show_menu():
    """Display the calculator menu."""
    print("----------- MENU -----------")
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")
    print()
    print("----------------------------")
    print()


def get_number(prompt):
    """
    Ask the user for a number and keep asking until a valid number is entered.
    Supports both integers and decimal numbers (float).
    Uses try/except to handle invalid input like 'abc'.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print()
            print("Invalid input!")
            print("Please enter a valid number.")
            print()


# --- Arithmetic Functions ---
# Each function takes two numbers (parameters) and returns the result.

def add(a, b):
    """Return sum of a and b."""
    return a + b


def subtract(a, b):
    """Return subtraction of b from a."""
    return a - b


def multiply(a, b):
    """Return multiplication of a and b."""
    return a * b


def divide(a, b):
    """
    Return division of a by b.
    Returns None if b is zero to signal an error.
    Caller must check for None before printing result.
    """
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    """
    Return remainder of a divided by b.
    Returns None if b is zero.
    """
    if b == 0:
        return None
    return a % b


def power(a, b):
    """Return a raised to the power of b (a ** b)."""
    return a ** b


def format_result(value):
    """
    Format number nicely for display.
    Uses :g to remove trailing zeros: 40.0 -> 40, 12.5 stays 12.5
    """
    # :g formatting works for both int and float
    return f"{value:g}"


def calculator():
    """Main calculator loop - shows menu and handles user choices."""
    # Welcome message - shown once at start
    print("=================================")
    print("       PYTHON CALCULATOR")
    print("=================================")
    print()
    print("Welcome to the Python Calculator!")
    print()

    # Loop forever until user chooses Exit (7)
    while True:
        show_menu()

        # Get user choice - handle non-numeric input with try/except
        choice_input = input("Enter your choice: ")
        choice_input = choice_input.strip()

        try:
            choice = int(choice_input)
        except ValueError:
            print()
            print("Invalid choice!")
            print("Please select an option from 1 to 7.")
            print()
            continue

        # Exit option
        if choice == 7:
            print()
            print("Thank you for using Python Calculator!")
            print("Goodbye!")
            break

        # Validate choice is 1-6
        if choice < 1 or choice > 7:
            print()
            print("Invalid choice!")
            print("Please select an option from 1 to 7.")
            print()
            continue

        # For operations 1-6, get two numbers
        print()
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        # Perform the selected operation using if/elif
        result = None
        error = None

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
            if result is None:
                error = "Error: Cannot divide by zero."
        elif choice == 5:
            result = modulus(num1, num2)
            if result is None:
                error = "Error: Cannot divide by zero."
        elif choice == 6:
            result = power(num1, num2)

        # Display result or error
        print()
        if error:
            print(error)
        else:
            print(f"Result: {format_result(result)}")
        print()


def main():
    """Entry point of the program."""
    calculator()


# This is the Python main pattern.
# It means: only run main() when this file is executed directly,
# not when it is imported by another file.
if __name__ == "__main__":
    main()
