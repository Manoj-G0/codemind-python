n=int(input())
a=1
b=1
for i in range(n):
    for i in range(n-1,i,-1):
        print(" ",end="")
    for k in range(1,a+1):
        print(abs(k-b),end="")
    a+=2
    b+=1
    print()