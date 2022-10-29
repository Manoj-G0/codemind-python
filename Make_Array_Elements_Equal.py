n=int(input())
a=list(map(int,input().split()))
b=[]
if a.count(a[0])==n:
    print(0)
else:
    for i in a:
        b.append(a.count(i))
    print(max(b))