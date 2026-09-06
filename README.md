# Python Calculator

A beginner-friendly command-line calculator built with Python.

## Description

Simple Python Calculator is a terminal-based application that allows users to perform basic mathematical operations. It is designed as a first Python project to learn core concepts like variables, functions, loops, conditionals, and error handling. The program runs in a loop until the user chooses to exit, handling invalid input gracefully without crashing.

## Features

- **Addition** — Add two numbers (`10 + 5 = 15`)
- **Subtraction** — Subtract second number from first (`10 - 5 = 5`)
- **Multiplication** — Multiply two numbers (`10 × 5 = 50`)
- **Division** — Divide first number by second with zero-division protection
- **Modulus** — Remainder after division (`10 % 3 = 1`) with zero protection
- **Power** — Raise first number to the power of second (`2 ^ 5 = 32`)
- **Exit** — Gracefully exit the calculator
- Supports integers, decimals, and negative numbers
- Input validation for numbers and menu choices
- Continuous loop until exit

## Technologies

- Python 3 (3.6+ recommended)
- Python Standard Library only — no external packages

## Installation

1. **Install Python** — Download from [python.org](https://www.python.org/downloads/)
2. Verify installation:

```bash
python --version
# or
python3 --version
```

3. Clone or download this repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-calculator.git
cd python-calculator
```

No additional dependencies to install — `requirements.txt` is empty because only the standard library is used.

## How to Run

```bash
python calculator.py
```

On some systems (macOS / Linux) use:

```bash
python3 calculator.py
```

## Usage

1. Run the program — you will see the welcome message and menu.
2. Enter a choice from `1` to `7`.
3. For choices `1–6`, enter two numbers when prompted.
4. View the result, then you return to the menu automatically.
5. Choose `7` to exit.

### Menu

```
----------- MENU -----------

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Exit

----------------------------
```

## Example

```
=================================
       PYTHON CALCULATOR
=================================

Welcome to the Python Calculator!

----------- MENU -----------

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Exit

----------------------------

Enter your choice: 1

Enter first number: 25
Enter second number: 15

Result: 40

----------- MENU -----------

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Exit

----------------------------

Enter your choice: 4

Enter first number: 10
Enter second number: 0

Error: Cannot divide by zero.

----------- MENU -----------

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Exit

----------------------------

Enter your choice: 7

Thank you for using Python Calculator!
Goodbye!
```

## Testing

Manual testing checklist — try these in the running program:

### Addition
- `10 + 5 = 15`
- `-5 + 10 = 5`
- `2.5 + 2.5 = 5`

### Subtraction
- `10 - 5 = 5`
- `5 - 10 = -5`

### Multiplication
- `10 × 5 = 50`
- `2.5 × 4 = 10`

### Division
- `10 / 2 = 5`
- `10 / 0` → `Error: Cannot divide by zero.`

### Modulus
- `10 % 3 = 1`
- `10 % 0` → `Error: Cannot divide by zero.`

### Power
- `2 ^ 3 = 8`
- `5 ^ 0 = 1`

### Invalid Input
- Enter `abc`, `hello`, `!!!` when a number is expected → `Invalid input! Please enter a valid number.`
- Enter `hello` for menu choice → `Invalid choice! Please select an option from 1 to 7.`

### Invalid Menu Choice
- Enter `0`, `8`, `100` → `Invalid choice! Please select an option from 1 to 7.`

## Project Structure

```
python-calculator/
│
├── calculator.py      # Main calculator application
├── README.md          # Project documentation
├── requirements.txt   # Dependencies (none - standard library only)
└── .gitignore         # Git ignore rules for Python
```

## Code Overview

| Function | Purpose |
|----------|---------|
| `show_menu()` | Prints the menu |
| `get_number()` | Gets and validates numeric input with try/except |
| `add(a, b)` | Returns `a + b` |
| `subtract(a, b)` | Returns `a - b` |
| `multiply(a, b)` | Returns `a * b` |
| `divide(a, b)` | Returns `a / b` or `None` if dividing by zero |
| `modulus(a, b)` | Returns `a % b` or `None` if modulo by zero |
| `power(a, b)` | Returns `a ** b` |
| `calculator()` | Main loop: welcome → menu → choice → operation → result |
| `main()` | Entry point, calls `calculator()` |

## Future Improvements

- Calculation history (show last N calculations)
- Scientific calculator mode (sqrt, log, sin/cos)
- Percentage calculation
- Square root
- User-defined formulas
- GUI version using Tkinter
- Saving calculation history to a file
- Support for more than two operands or chained operations

## License

MIT License — feel free to use and modify for learning.

---

**Suggested GitHub topics:** `python` `calculator` `beginner-project` `python-project` `cli` `learning-python`
