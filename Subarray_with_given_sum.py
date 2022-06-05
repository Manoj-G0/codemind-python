def sarray(a,n,k):
    c=0
    for i in range(n):
        temp=a[i]
        for j in range(i+1,n+1):
            if temp==k:
                print(i+1,j)
                return 1
            if temp>k or j==n:
                break
            temp+=a[j]
    print(-1)
    return 0


t=int(input())
while(t):
    t-=1
    c=0
    n,k=map(int,input().split())
    a= list(map(int,input().split()))
    sarray(a,n,k)