# Implementation of MD5 Hash Function using hashlib

import hashlib

def md5_hash():
    print("=== MD5 Hash Function ===")
    message = input("Enter message: ").encode()       # convert to bytes
    md5_hash = hashlib.md5(message).hexdigest()        # compute MD5
    print("\nOriginal Message:", message.decode())
    print("MD5 Hash (128-bit):", md5_hash)
    print("Length of hash:", len(md5_hash)*4, "bits")  # 32 hex digits = 128 bits

# Run the program
md5_hash()
