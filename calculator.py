def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    print(">>> Super Calculator: Version B <<<")
print("=== Team Calculator: Version A ===")

def divide(a, b):
    if b == 0: 
        return "Error: Division by zero"
    return a / b

def calculate():
    print("Welcome to the Pair Calculator!")
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))
    print("Multiplication: 5 * 3 =", multiply(5, 3))
    print(">>> Super Calculator: Version B <<<")

if __name__ == "__main__":
    calculate()