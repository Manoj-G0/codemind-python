s=input()
k=input()
s=s.lower()
k=k.lower()
s=s.split(" ")
k=k.split(" ")
t=[]
r=[]
c=0
for i in range(len(s)):
    if s.count(s[i])==1:
        r.append(s[i])
for i in range(len(k)):
    if k.count(k[i])==1:
        t.append(k[i])
for i in t:
    if i in r:
        c+=1
print(c)
