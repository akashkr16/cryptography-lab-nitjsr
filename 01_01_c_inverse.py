#Extended Euclidean algorithm

def mod_inverse(a,p):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd, a, y

#Function to find modular inverse
def mod_inverse(a, p):
    gcd, x, _ = extended_euclidean(a, p)
    if gcd != 1:       # <-- indented inside function
        return None
    else:              # <-- also indented inside function
        return x % p
