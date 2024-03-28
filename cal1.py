def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

operations = {
    'addition': add,
    'subtraction': subtract,
    'multiplication': multiply,
    'division': divide,
}

print("Select operation:")
for key in operations:
    print(f"{key.capitalize()}")
    choice = input("Enter operation name: ").lower()

    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = operations[choice](num1, num2)
        print(f"\nOperation: {choice.capitalize()}")
        print(f"Result: {result}")
    else:
        print("Invalid operation name")