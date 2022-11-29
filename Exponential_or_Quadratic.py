def powe(a,b):
    if b==0:
        return 1
    res=powe(a,b//2)
    if b%2==0:
        return res*res
    return res*res*a

n=int(input())
if n>10 or powe(2,n) > n*n:
    print("Yes")
else:
    print("No")