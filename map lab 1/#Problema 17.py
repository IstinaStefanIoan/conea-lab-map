#Problema 17
a=int(input("Introduceti primul unghi din triunghi. "))
b=int(input("Introduceti al doilea unghi. "))
c=int(input("Introduceti al treilea unghi. "))
ok=1
if(a+b+c!=180 or 180-a-b!=c or 180-b-c!=a or 180-a-c!=b):
    ok=0
if(ok==1):
    print("Exista triunghi")
else:
    print("Nu exista triunghi")