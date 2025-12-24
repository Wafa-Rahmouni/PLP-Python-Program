def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+ for sum, - for substraction, * for multiplication, / for division): ")
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please use one of: +, -, *, /")
            return
            
        # Display result
        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")

# Run the calculator
if __name__ == "__main__":
    calculator()
