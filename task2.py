def main():
    # Prompt user for the first number
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Prompt user for the second number
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Display operation choices
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt user for operation choice
    operation = input("Enter choice (1/2/3/4): ")

    # Perform calculation based on choice
    if operation == '1':
        result = num1 + num2
        operator = '+'
    elif operation == '2':
        result = num1 - num2
        operator = '-'
    elif operation == '3':
        result = num1 * num2
        operator = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        operator = '/'
    else:
        print("Invalid operation choice.")
        return

    # Display the result
    print(f"\nResult: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()