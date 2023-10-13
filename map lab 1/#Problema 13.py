#Problema 13
n=int(input("Introduceti cate valori in lista, n= "))
v=[]
for i in range(0,n,1):
    val=int(input("v["+str(i)+"]="))
    v.append(val)
s=0
for i in range(0,n,1):
    s+=v[i]
print("Suma=",s)
print("Media=",s/n)