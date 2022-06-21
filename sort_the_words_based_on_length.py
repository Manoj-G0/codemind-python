s=input().split(" ")
s=sorted(s)
for i in range(1, len(s)):
    temp=s[i]
    j=i-1
    while j>=0 and len(temp)<len(s[j]):
        s[j+1]=s[j]
        j-=1
    s[j+1]=temp
print(*s)