# Fermat's Primality Test

def power_mod(a, d, n):
    result = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % n
        d //= 2
        a = (a * a) % n
    return result

n = int(input("Enter number to test: "))
a = int(input("Enter base a (1 < a < n): "))

if power_mod(a, n - 1, n) == 1:
    print(n, "is probably Prime (Fermat test passes for base", a, ")")
else:
    print(n, "is Composite")
