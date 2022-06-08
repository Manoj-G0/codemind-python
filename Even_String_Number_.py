s=input()
a=[]
b=[]
c=0
k=0
m=1000
for i in range(len(s)):
    if s[i].isdigit():
        b.append(int(s[i]))
for i in b:
    if i not in a:
        a.append(i)
for i in range(len(a)):
    if a[i]%2==0 and m>a[i]:
        c+=1
        m=a[i]
        k=i
if c==0:
    print("-1")
else:
    a.remove(m)
    a.sort(reverse=True)
    for i in range(0,len(a)):
        print(a[i],end="")
    print(m)