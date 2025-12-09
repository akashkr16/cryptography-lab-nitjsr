# Playfair Cipher

def generate_playfair_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    matrix = ""
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in matrix:
            matrix += c
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace("J", "I")
    text = "".join([c for c in text if c.isalpha()])
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) and text[i+1] != a else "X"
        pairs.append(a+b)
        i += 2 if b != "X" else 1
    
    result = ""
    for pair in pairs:
        a, b = pair[0], pair[1]
        ai, aj, bi, bj = None, None, None, None
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a: ai, aj = r, c
                if matrix[r][c] == b: bi, bj = r, c
        if ai == bi:
            result += matrix[ai][(aj+1)%5] + matrix[bi][(bj+1)%5]
        elif aj == bj:
            result += matrix[(ai+1)%5][aj] + matrix[(bi+1)%5][bj]
        else:
            result += matrix[ai][bj] + matrix[bi][aj]
    return result

# -------- Main Program --------
text = input("Enter plaintext: ")
key = input("Enter Playfair key: ")

encrypted = playfair_encrypt(text, key)
print("Encrypted:", encrypted)
