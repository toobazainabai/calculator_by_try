def main():
    calculator()

def calculator():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            operator = input("Enter an operator (+, -, *, /): ").strip()
            num2 = int(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            continue

        except ValueError as ve:
            print(f"Error: {ve}")
            continue
        
        print(f"The result is: {result}")

        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for using the calculator!")
            break

main()
