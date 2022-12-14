notes=[]
x,y = map(int, input().split())

if y>x:
    print(-1)
    exit()
else:
    for i in range(x):
        for j in range(x//2):
            if i+2*j==x and (i+j)%y==0:
                notes.append(i)
                notes.append(j)
                break
a=notes[0]
b=notes[1]
print(a+b)
