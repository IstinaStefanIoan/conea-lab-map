#Probleme 5
a=int(input("Introduceti a= "))
i=2
p=1
if(a==0):
    print(1)
else:
    while i<=a:
        p*=i
        i+=1
    print(p)