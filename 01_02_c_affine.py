# Affine Cipher

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr(((a * (ord(char) - shift) + b) % 26) + shift)
        else:
            result += char
    return result

def affine_decrypt(text, a, b):
    # Find modular inverse of a mod 26
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    else:
        return "No inverse exists for key a."
    
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((a_inv * (ord(char) - shift - b)) % 26 + shift)
        else:
            result += char
    return result

# -------- Main Program --------
text = input("Enter plaintext: ")
a = int(input("Enter key a (must be coprime with 26): "))
b = int(input("Enter key b: "))

encrypted = affine_encrypt(text, a, b)
decrypted = affine_decrypt(encrypted, a, b)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
