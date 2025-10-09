# Diffie-Hellman Key Exchange Implementation

# Step 1: Publicly known values
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root of p (g): "))

# Step 2: Private keys (chosen secretly)
a = int(input("Enter private key for Alice (a): "))
b = int(input("Enter private key for Bob (b): "))

# Step 3: Compute public keys
A = (g ** a) % p  # Alice's public key
B = (g ** b) % p  # Bob's public key

print("\nPublic key of Alice (A):", A)
print("Public key of Bob (B):", B)

# Step 4: Exchange public keys and compute shared secret
shared_key_Alice = (B ** a) % p
shared_key_Bob = (A ** b) % p

print("\nShared key (computed by Alice):", shared_key_Alice)
print("Shared key (computed by Bob):", shared_key_Bob)

# Step 5: Verify both are equal
if shared_key_Alice == shared_key_Bob:
    print("\n✅ Key exchange successful!")
    print("Shared Secret Key:", shared_key_Alice)
else:
    print("\n❌ Key exchange failed.")
