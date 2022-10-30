t=int(input())
while t:
    t-=1
    a=[]
    n=int(input())
    for i in range(n,-1,-1):
        if i&(i-1)==0:
            print(i)
            break