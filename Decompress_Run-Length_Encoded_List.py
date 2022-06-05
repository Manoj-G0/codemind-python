n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(n//2):
    s+=a[2*i]*[a[2*i+1]]
print(*s)