a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b if b != 0 else 'Undefined (Div by 0)'}")
print(f"Mod: {a % b if b != 0 else 'Undefined (Div by 0)'}")