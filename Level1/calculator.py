# Level 1 - Task 1
# Simple Calculator Application
# Codveda Python Internship

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def calculator():
    while True:
        print("\n===== Simple Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 5:
                print("Thank you for using the calculator!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice! Please select a valid option.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subtract(num1, num2))
            elif choice == 3:
                print("Result:", multiply(num1, num2))
            elif choice == 4:
                print("Result:", divide(num1, num2))

        except ValueError:
            print("Error: Please enter valid numeric values.")

calculator()
