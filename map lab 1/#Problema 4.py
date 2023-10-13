#Problema 4
a=float(input("Introduceti a: "))
b=float(input("Introduceti b: "))
if a<b:
    aux=a
    a=b
    b=aux
if(a==0 or b==0):
    print("Nu se poate impartii la 0")
else:
    while b:
        r=a%b
        a=b
        b=r
    print(a)