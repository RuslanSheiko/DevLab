class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"

if __name__ == "__main__":
    calculator = Calculator()

    while True:
        try:
            expression = input("Enter expression (e.g., 2 + 3, type 'exit' to quit): ")
            
            if expression.lower() == 'exit':
                break
            
            parts = expression.split()
            
            if len(parts) != 3:
                print("Invalid expression. Please enter a valid expression.")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == '+':
                result = calculator.add(num1, num2)
            elif operator == '-':
                result = calculator.subtract(num1, num2)
            elif operator == '*':
                result = calculator.multiply(num1, num2)
            elif operator == '/':
                result = calculator.divide(num1, num2)
            else:
                print("Invalid operator. Please enter a valid operator (+, -, *, /).")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print("An error occurred:", str(e))
