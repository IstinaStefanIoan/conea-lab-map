#Problema 12
n=int(input("Scrieti al catalea numar din sirul fibonacci doriti. "))
a=0
b=1
for i in range(0,n,1):
    print(a)
    s=a+b
    a=b
    b=s