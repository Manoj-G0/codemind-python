def isprime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
n=int(input())
if(isprime(n)):
    print("prime")
else:
    print("not a prime")