#Problema 14
n=int(input("Introduceti cate valori in lista, n= "))
v=[]
for i in range(0,n,1):
    val=int(input("v["+str(i)+"]="))
    v.append(val)
mic=v[0]
mare=v[0]
for i in range (1,n,1):
    if v[i]>mare:
        mare=v[i]
    if v[i]<mic:
        mic=v[i]
print("Cel mai mare numar din lista este ",mare)
print("Cel mai mic numar din lista este",mic)