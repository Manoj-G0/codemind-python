n=int(input())
a=list(map(int,input().split()))
c,k=0,0
for i in a:
    if i%2==1:
        c+=1
    else:
        k+=1
if c%2==0 or k%2==0:
    print(1)
else:
    print(0)