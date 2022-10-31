def isdist(s,r,c):
    k=[0]*123
    for i in range(r,c+1):
        if(k[ord(s[i])]==True):
            return False
        k[ord(s[i])]=True
    return True
        
s=input()
k=s.lower()
n=len(s)
res=0
init=0
c=0
m=0
d={}
for i in range(n):
    if k[i] not in d:
        d[k[i]]=i
    else:
        if d[k[i]]>=c:
            l=i-c
            if l>m:
                m=l
                init=c
            c=d[k[i]]+1
        d[k[i]]=i
l=i-c
if l>m:
    m=l
    init=c
if m>=3:
    print(s[init:init+m])
else:
    print(-1)
            
            
            
            