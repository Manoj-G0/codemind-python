n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if a.count(-1)==b.count(-1):
    print("Infinite")
elif a.count(-1)==2:
    print(max(0,sum(b)-sum(a)-1))
elif b.count(-1)==2:
    print(max(0,sum(a)-sum(b)-1))
elif a.count(-1)==1:
    if sum(b)>=sum(a):
        print(1)
    else:
        print(0)
else:
    if sum(a)>=sum(b):
        print(1)
    else:
        print(0)