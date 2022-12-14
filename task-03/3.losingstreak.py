fact1=[]
fact2=[]
result=[]
def factors(n):
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                yield i
                break
x,y = map(int, input().split())
if x==y:
    print("0")
elif int(y)%int(x)==0: 
    for i in factors(y):
        fact1.append(i)
    for i in factors(x):
        fact2.append(i)
    for i in fact2:
        fact1.remove(i)
    print((len(fact1)))
elif int(y)%int(x)!=0:
    print("-1")
