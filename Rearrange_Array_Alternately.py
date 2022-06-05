t=int(input())
while(t):
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    high=n-1
    low=0
    flag=1
    k=n*[0]
    for i in range(n):
        if flag==1:
            k[i]=a[high]
            high-=1
        else:
            k[i]=a[low]
            low+=1
        flag= not(flag)
    print(*k)