#Implementation of Extended Euclidean Algorithm

def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd, x, y

# Example
a, b = map(int, input("Enter two numbers: ").split())
gcd, x, y = extended_euclidean(a, b)
print(f"GCD({a}, {b}) = {gcd}")
print(f"Coefficients: x = {x}, y = {y}  (i.e., {a}*{x} + {b}*{y} = {gcd})")
