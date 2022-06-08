s=input()
a=[]
p1=0
p2=len(s)
for i in range(len(s)):
    if s[i]=='I':
        a.append(p1)
        p1+=1
    else:
        a.append(p2)
        p2-=1
a.append(p1)
print(*a)