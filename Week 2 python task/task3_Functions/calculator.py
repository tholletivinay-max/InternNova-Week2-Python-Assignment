# Function for addition
def addition(a, b):
    return a + b


# Function for subtraction
def subtraction(a, b):
    return a - b


# Function for multiplication
def multiplication(a, b):
    return a * b


# Function for division
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# Function for modulus
def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the results
print("Addition:", addition(num1, num2))
print("Subtraction:", subtraction(num1, num2))
print("Multiplication:", multiplication(num1, num2))
print("Division:", division(num1, num2))
print("Modulus:", modulus(num1, num2))