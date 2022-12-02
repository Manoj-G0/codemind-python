def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
n=int(input())
a=list(map(int,input().split()))
m=1e9+7
for i in range(n-1):
    m=min(m,gcd(a[i],a[i+1]))
print(m*n)

    
