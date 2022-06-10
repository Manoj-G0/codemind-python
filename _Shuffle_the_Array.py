n=int(input())
a=list(map(int,input().split()))
i=0
j=n//2
while i!=j and j!=n:
    print(a[i],end=" ")
    print(a[j],end=" ")
    i+=1
    j+=1
    