# Multiplicative Cipher

def multiplicative_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr(((ord(char) - shift) * key) % 26 + shift)
        else:
            result += char
    return result

def multiplicative_decrypt(text, key):
    # Find modular inverse of key mod 26
    for i in range(26):
        if (key * i) % 26 == 1:
            inv = i
            break
    else:
        return "No inverse exists for this key."
    
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr(((ord(char) - shift) * inv) % 26 + shift)
        else:
            result += char
    return result

# -------- Main Program --------
text = input("Enter plaintext: ")
key = int(input("Enter key (must be coprime with 26): "))

encrypted = multiplicative_encrypt(text, key)
decrypted = multiplicative_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

