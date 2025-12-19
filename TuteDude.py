n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

add = n1 + n2
sub = n1 - n2
multi = n1 * n2

if n2 != 0:
    division = n1 / n2
else:
    division = "Undefined (cannot divide by zero)"

print("\n--- Results ---")
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {multi}")
print(f"Division: {division}")