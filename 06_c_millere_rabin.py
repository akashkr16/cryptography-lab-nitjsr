# Miller–Rabin Primality Test

def power_mod(a, d, n):
    result = 1
    a = a % n
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % n
        d //= 2
        a = (a * a) % n
    return result

def miller_rabin(n, a_values):
    # write n-1 = 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for a in a_values:
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

n = int(input("Enter number to test: "))
bases = [2, 3, 5, 7]

if miller_rabin(n, bases):
    print(n, "is a probable Prime")
else:
    print(n, "is Composite")
