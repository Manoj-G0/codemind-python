a=input()
b=input()
c=0
s=""
k=""
for i in a:
    if i not in s and i!=" ":
        s+=i
for i in b:
    if i not in k and i!=" ":
        k+=i
s=s.lower()
k=k.lower()
for i in k:
    if i in s:
        c+=1
print(c)