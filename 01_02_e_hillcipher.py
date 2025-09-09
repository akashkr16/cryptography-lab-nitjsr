#Name: AKASH KUMAR
#ROLL NO: 2025PGCSIS09


# Hill Cipher (2x2)

import numpy as np

def hill_encrypt(text, key_matrix):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"  # padding
    
    result = ""
    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - 65, ord(text[i+1]) - 65]
        res = np.dot(key_matrix, pair) % 26
        result += chr(res[0] + 65) + chr(res[1] + 65)
    return result

# -------- Main Program --------
text = input("Enter plaintext: ")
print("Enter 2x2 key matrix (row by row):")
k11 = int(input("k11: ")); k12 = int(input("k12: "))
k21 = int(input("k21: ")); k22 = int(input("k22: "))
key_matrix = np.array([[k11, k12], [k21, k22]])

encrypted = hill_encrypt(text, key_matrix)
print("Encrypted:", encrypted)
