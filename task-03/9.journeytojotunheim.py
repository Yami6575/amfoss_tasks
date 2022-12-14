t=int(input(""))
result=[]

for i in range(t):
    key=[]
    n=int(input(""))
    key=map(int,input("").split(" ",3))
    portal=list(key)
    
    if portal[n-1]!=0:
        poor=int(portal[n-1])
        if portal[poor-1]!=0:
            result.append("YES")
        else:
            result.append("NO")
            
    else:
        result.append("NO")
for i in range(t):
    print(result[i])
