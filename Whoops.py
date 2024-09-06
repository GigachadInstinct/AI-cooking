import math
import cmath

class AdvancedCalculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, a, b):
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result

    def square_root(self, a):
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result

    def logarithm(self, a, base=math.e):
        result = math.log(a, base)
        self.history.append(f"log_{base}({a}) = {result}")
        return result

    def sine(self, angle):
        result = math.sin(math.radians(angle))
        self.history.append(f"sin({angle}°) = {result}")
        return result

    def cosine(self, angle):
        result = math.cos(math.radians(angle))
        self.history.append(f"cos({angle}°) = {result}")
        return result

    def tangent(self, angle):
        result = math.tan(math.radians(angle))
        self.history.append(f"tan({angle}°) = {result}")
        return result

    def factorial(self, n):
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result

    def solve_quadratic(self, a, b, c):
        discriminant = b**2 - 4*a*c
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        self.history.append(f"Quadratic equation {a}x^2 + {b}x + {c} = 0")
        self.history.append(f"Solutions: x1 = {root1}, x2 = {root2}")
        return root1, root2

    def store_in_memory(self, value):
        self.memory = value
        self.history.append(f"Stored {value} in memory")

    def recall_memory(self):
        self.history.append(f"Recalled {self.memory} from memory")
        return self.memory

    def clear_memory(self):
        self.memory = 0
        self.history.append("Cleared memory")

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []

def main():
    calc = AdvancedCalculator()
    print("Welcome to the Advanced Calculator!")
    
    while True:
        print("\nAvailable operations:")
        print("1. Add\t\t2. Subtract\t3. Multiply\t4. Divide")
        print("5. Power\t6. Square Root\t7. Logarithm\t8. Sine")
        print("9. Cosine\t10. Tangent\t11. Factorial\t12. Solve Quadratic")
        print("13. Store in Memory\t14. Recall Memory\t15. Clear Memory")
        print("16. Show History\t17. Clear History\t18. Exit")

        choice = input("Enter your choice (1-18): ")

        if choice == '18':
            print("Thank you for using the Advanced Calculator. Goodbye!")
            break

        try:
            if choice in ['1', '2', '3', '4', '5']:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if choice == '1':
                    print("Result:", calc.add(a, b))
                elif choice == '2':
                    print("Result:", calc.subtract(a, b))
                elif choice == '3':
                    print("Result:", calc.multiply(a, b))
                elif choice == '4':
                    print("Result:", calc.divide(a, b))
                elif choice == '5':
                    print("Result:", calc.power(a, b))

            elif choice in ['6', '7', '8', '9', '10', '11']:
                a = float(input("Enter a number: "))
                if choice == '6':
                    print("Result:", calc.square_root(a))
                elif choice == '7':
                    base = float(input("Enter logarithm base (or press Enter for natural log): ") or math.e)
                    print("Result:", calc.logarithm(a, base))
                elif choice == '8':
                    print("Result:", calc.sine(a))
                elif choice == '9':
                    print("Result:", calc.cosine(a))
                elif choice == '10':
                    print("Result:", calc.tangent(a))
                elif choice == '11':
                    print("Result:", calc.factorial(int(a)))

            elif choice == '12':
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter coefficient c: "))
                root1, root2 = calc.solve_quadratic(a, b, c)
                print(f"Roots: x1 = {root1}, x2 = {root2}")

            elif choice == '13':
                value = float(input("Enter value to store in memory: "))
                calc.store_in_memory(value)
                print("Value stored in memory")

            elif choice == '14':
                print("Value in memory:", calc.recall_memory())

            elif choice == '15':
                calc.clear_memory()
                print("Memory cleared")

            elif choice == '16':
                history = calc.get_history()
                print("\nCalculation History:")
                for item in history:
                    print(item)

            elif choice == '17':
                calc.clear_history()
                print("History cleared")

        except ValueError as e:
            print("Error:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    main()