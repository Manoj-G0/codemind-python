n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(1,n):
    s.append(max(a[i:]))
s.append(-1)
print(*s)