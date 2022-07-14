r,c=map(int,input().split())
b=[]
for i in range(r):
    a=list(map(int,input().split()))
    b.append(a)
for i in range(c):
    m=0
    for j in range(r):
        m=max(m,b[j][i])
    print(m)