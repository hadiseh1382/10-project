import random

X = random.randint(0, 10)
P = X
A = 0  # مقدار اولیه A را برابر با یک عدد خارج از محدوده قرار دهید

while A != P:
    A = int(input("عدد چند است؟ "))
    if A == P:
        print("آفرین درست حدس زدی")
    elif A < P:
        print(A, "کوچک است")
    elif A > P:
        print(A, "بزرگ است")