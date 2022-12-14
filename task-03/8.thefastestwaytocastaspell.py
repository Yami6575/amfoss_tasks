n=input()
a=[]
a=n.split()
l=[]
for i in range(int(a[1])):
    k=[]
    st=input()
    k=st.split()
    l.append(k)
spell=input()
spells=spell.split()
finallist=[]
for j in spells:
    for m in l:
        if m[0]==j:
            if len(m[0])<=len(m[1]):
                finallist.append(m[0])
                break
            else:
                finallist.append(m[1])
                break
        else:
            continue
for i in range(int(a[0])):
    print(finallist[i],end=" ")
