#implementation of euclidean algorithm (gcd)


def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example
x, y = map(int, input("Enter two numbers: ").split())
print(f"GCD({x}, {y}) = {euclidean_algorithm(x, y)}")

