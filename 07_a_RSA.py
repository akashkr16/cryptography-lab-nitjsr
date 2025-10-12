# RSA Algorithm Implementation (No external library)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Find d such that (d*e) % phi = 1
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Step 1: Input two primes
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

# Step 2: Compute n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose e (public exponent)
for e in range(2, phi):
    if gcd(e, phi) == 1:
        break

# Step 4: Find d (private exponent)
d = mod_inverse(e, phi)

# Step 5: Display keys
print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Step 6: Encryption
msg = int(input("\nEnter message (as number): "))
cipher = pow(msg, e, n)
print("Encrypted message:", cipher)

# Step 7: Decryption
decrypted = pow(cipher, d, n)
print("Decrypted message:", decrypted)
