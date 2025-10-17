# Primality Test using Division Algorithm

n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(n, "is Prime")
    else:
        print(n, "is Not Prime")
