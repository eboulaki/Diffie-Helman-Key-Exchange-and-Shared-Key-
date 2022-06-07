p=17
g=4
a=int(input("Enter Alice's private key: "))
b=int(input("Enter Bob's private key: "))
A = ((pow(g, a)) % p)
B = ((pow(g, b)) % p)
Ka = ((pow(B, a)) % p)
Kb = ((pow(A, b)) % p)
if (Ka==Kb):
    print("Secret Key:",Kb)
else:
    print("Error")