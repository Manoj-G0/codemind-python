t=int(input())
while t:
    t-=1 
    n=int(input())
    k=1
    while True:
        if k*2>n:
            print(k-1)
            break
        k*=2
    