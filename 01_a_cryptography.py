# AKASH KUMAR (2025PGCSIS09)
# implementation of euclidean algorithm (gcd)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Output
print(f"GCD of {a} and {b} is: {gcd(a, b)}")

