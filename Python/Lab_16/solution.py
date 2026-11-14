# Simplified Utility Calculator

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else None
def power(base, exp=2): return base ** exp

def main():
    history = []
    
    while True:
        print("\n--- SIMPLE CALCULATOR ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. View History")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ")
        
        if choice == '7':
            print("Goodbye!")
            break
            
        if choice == '6':
            print("\nHistory:")
            for item in history:
                print(item)
            continue
            
        if choice in ('1', '2', '3', '4', '5'):
            a = float(input("Enter first number: "))
            
            if choice == '5':
                result = power(a)
                record = f"{a} ^ 2 = {result}"
            else:
                b = float(input("Enter second number: "))
                if choice == '1':
                    result, record = add(a, b), f"{a} + {b} = {add(a, b)}"
                elif choice == '2':
                    result, record = subtract(a, b), f"{a} - {b} = {subtract(a, b)}"
                elif choice == '3':
                    result, record = multiply(a, b), f"{a} * {b} = {multiply(a, b)}"
                elif choice == '4':
                    result = divide(a, b)
                    if result is None:
                        print("Error: Cannot divide by zero!")
                        continue
                    record = f"{a} / {b} = {result}"
            
            print(f"Result: {result}")
            history.append(record)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()