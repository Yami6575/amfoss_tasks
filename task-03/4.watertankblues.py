tank=[]
slist=[]
t=int(input(""))
for i in range(t):
    f=0
    n=int(input(""))
    tank=map(int,input().split(" ",n-1))
    f=list(tank)
    j=0
    while f[j]==0:
        j=j+1
    tank=f[j:n-1]
    zero=tank.count(0)
    f=sum(tank)
    slist.append(f+zero)
for i in range(t):
    print(slist[i])
