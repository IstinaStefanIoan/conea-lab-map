#Problema 6
x=int(input("Numarul x="))
chk=2
if(x>2):
    for i in range(2,x,1):
        if(x%i==0):
            chk+=1
if(chk==2):
    print("x este prim")
else:
    print("x nu este prim")