# Simple Calculator Project using Operators

def calculator():
    print("===== Simple Calculator =====")
    
    # Taking two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Menu
    print("\nChoose Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
    
    choice = int(input("\nEnter your choice (1-7): "))
    
    result = None   # variable to store result
    
    # Using Arithmetic Operators
    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        # Relational + Logical operator to avoid zero division
        if num2 != 0:
            result = num1 / num2
        else:
            print("⚠ Division by zero not allowed!")
    elif choice == 5:
        result = num1 % num2
    elif choice == 6:
        result = num1 ** num2
    elif choice == 7:
        result = num1 // num2
    else:
        print("❌ Invalid choice!")
    
    # Display result if calculated
    if result is not None:
        print(f"\n✅ Result: {result}")

# Run Project
calculator()
