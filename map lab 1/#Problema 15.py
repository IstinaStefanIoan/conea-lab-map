#Problema 15
v=[]
for i in range(8):
    val=int(input("v["+str(i)+"]="))
    v.append(val)
for i in range(0,8,1):
    swapped=False
    for j in range(1,8,1):
        if v[j]<v[j-1]:
            aux=v[j]
            v[j]=v[j-1]
            v[j-1]=aux
            swapped=True
        if swapped==False:
            break
for i in range(0,8,1):
    print(v[i])