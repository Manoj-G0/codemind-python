t=int(input())
k=1
while(t):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    m=0
    for i in range(0,n):
        if i==n-1 and a[i]>m:
            c+=1
        elif i==0 and a[i]>a[i+1]:
            c+=1
        elif a[i]>m and a[i]>a[i+1]:
            c+=1
        m=max(a[i],m)
    print("Case #%d:"%k,c)
    k+=1