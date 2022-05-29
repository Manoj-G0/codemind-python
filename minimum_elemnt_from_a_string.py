s=input()
k='z'
c=0
l=s.split(" ")
s=l[len(l)-1]  
for i in s:
    if i<=k:
        k=i
for i in range(len(s)):
    if ord(k)+32==ord(s[i]):
        c+=1
        print(s[i])
        break
if c==0:
    print(k)