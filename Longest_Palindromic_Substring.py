s=input()
m=0
k=0
for i in range(len(s)):
    l=i
    r=i+1
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>m:
            m=r-l+1
            k=l
        l-=1
        r+=1
for i in range(len(s)):
    l=i
    r=i
    while l>=0 and r<len(s) and s[l]==s[r]:
        if r-l+1>m:
            m=r-l+1
            k=l
        l-=1
        r+=1
for i in range(m):
    print(s[k],end="")
    k+=1

    