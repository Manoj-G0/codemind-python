s=[]
n=int(input())
for i in range(n):
    a=list(map(str,input().split()))
    s.append(a)
a=[]
b=[]
for i in s:
    a.append(i[0])
    b.append(i[1])
for i in b:
    if i not in a:
        print(i)
        break