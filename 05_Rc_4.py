# RC4 Stream Cipher Implementation

def KSA(key):
    """Key Scheduling Algorithm"""
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    """Pseudo-Random Generation Algorithm"""
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4_encrypt(key, plaintext):
    key_bytes = [ord(c) for c in key]
    S = KSA(key_bytes)
    keystream = PRGA(S)
    cipher = []
    for c in plaintext:
        cipher_byte = ord(c) ^ next(keystream)
        cipher.append("%02X" % cipher_byte)
    return ''.join(cipher)

def RC4_decrypt(key, ciphertext_hex):
    key_bytes = [ord(c) for c in key]
    S = KSA(key_bytes)
    keystream = PRGA(S)
    ciphertext = bytes.fromhex(ciphertext_hex)
    plaintext = ''.join(chr(c ^ next(keystream)) for c in ciphertext)
    return plaintext

# --- Main Program ---
key = input("Enter RC4 key: ")
message = input("Enter plaintext: ")

ciphertext = RC4_encrypt(key, message)
print("RC4 Encrypted (Hex):", ciphertext)

decrypted = RC4_decrypt(key, ciphertext)
print("RC4 Decrypted:", decrypted)
