num=input("")
res=list(map(int,num))

i=0
while len(res)!=1:
    
    afoo=sum(res)
    res=list(map(int,str(afoo)))
    i=i+1
print(i)
