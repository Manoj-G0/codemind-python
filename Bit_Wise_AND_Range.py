a,b=map(int,input().split())
c=0
while a!=b and a!=0:
    c+=1
    a=a>>1
    b=b>>1
print(a<<c)