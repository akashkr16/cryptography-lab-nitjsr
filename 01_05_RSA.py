#Name : Akash Kumar
#Roll no.: 2025PGCSIS09

import random

def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

def findE(x):
    valid_e = []
    for i in range(2, x):
        if((gcd(i,x)) == 1):
            valid_e.append(i)
            
    if(len(valid_e) != 0):
        return random.choice(valid_e)
    else:
        return None

def mod_inverse(e,x):
    for i in range(2,x):
        if(((i * e) % x) == 1):
            return i
    return None

def key_generation(a,b):
    n = a * b #will be used for mod n
    x = (a-1)*(b-1) #treat as phi(n)
    e = findE(x)
    d = mod_inverse(e,x) #mod inverse of e under phi(n) #d is the private key
    return (e,n),(d,n)

def fast_exponentiation(a, key):
    return pow(a, key[0], key[1])  

def RSA_encryption(text, key):
    cipher = []
    for ch in text:
        a = ord(ch) - ord('a')
        b = fast_exponentiation(a, key)
        cipher.append(b)
    return cipher

def RSA_decryption(cipher, key):
    plain = []
    for c in cipher:
        a = fast_exponentiation(c, key)
        plain.append(chr(a + ord('a')))
    return "".join(plain)

#taking input
a = int(input("Enter first prime number: "))
b = int(input("Enter second prime number: "))
pub, priv = key_generation(a,b)
text = input("Enter a plain text: ")
cipher = RSA_encryption(text, pub)
print(f"The cipher text for the text {text} is: ", " ".join(str(c) for c in cipher))
print("Decrypted text is:", RSA_decryption(cipher, priv))

#digital signature
signature = RSA_encryption(text, priv)
verified = RSA_decryption(signature, pub)

if text == verified:
    print("Yes, it is digital signature.")
else:
    print("No, it is not digital signature.")
