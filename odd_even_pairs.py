n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
if(n%2==0):
    for i in range(0,n):
        if(a[i]%2!=0):
            b.append(a[i])
        else:
            c.append(a[i])
    for i in range(len(a)):
        if i<len(b):
            print(b[i],end=" ")
        if i<len(c):
            print(c[i],end=" ")
        
else:
    for i in range(0,n):
        if(a[i]%2!=0):
            b.append(a[i])
        else:
            c.append(a[i])
    for i in range(len(a)):
        if i<len(b):
            print(b[i],end=" ")
        if i<len(c):
            print(c[i],end=" ")
    print(0) 
    
        
    