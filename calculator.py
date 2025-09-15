import math
def calculator():
    print("=== Scientific Calculator ===")
    print("Available operations: +, -, *, /, ^, %, sqrt")
    print("Type 'q' anytime to quit.\n")
    while True:
        # Get user input
        choice = input("Enter operation (+, -, *, /, ^, %, sqrt): ")
        if choice.lower() == "q":
            print(" Goodbye!")
            break
        # Square root only needs one number
        if choice == "sqrt":
            num = input("Enter a number: ")
            if num.lower() == "q":
                print(" Goodbye!")
                break
            try:
                num = float(num)
                if num < 0:
                    print("❌ Error: Cannot take square root of a negative number.\n")
                else:
                    print(f"✅ Result: sqrt({num}) = {math.sqrt(num)}\n")
            except ValueError:
                print("❌ Invalid input!\n")
            continue
        # Other operations need two numbers
        num1 = input("Enter first number: ")
        if num1.lower() == "q":
            print(" Goodbye!")
            break
        num2 = input("Enter second number: ")
        if num2.lower() == "q":
            print(" Goodbye!")
            break
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("❌ Invalid input! Please enter numbers.\n")
            continue
        # Perform operations
        if choice == "+":
            print(f"✅ Result: {num1} + {num2} = {num1 + num2}\n")
        elif choice == "-":
            print(f"✅ Result: {num1} - {num2} = {num1 - num2}\n")
        elif choice == "*":
            print(f"✅ Result: {num1} * {num2} = {num1 * num2}\n")
        elif choice == "/":
            if num2 == 0:
                print("❌ Error: Division by zero!\n")
            else:
                print(f"✅ Result: {num1} / {num2} = {num1 / num2}\n")
        elif choice == "^":
            print(f"✅ Result: {num1}^{num2} = {num1 ** num2}\n")
        elif choice == "%":
            print(f"✅ Result: {num1}% of {num2} = {(num1 / 100) * num2}\n")
        else:
            print("❌ Invalid operation! Try again.\n")
# Run program
calculator()

