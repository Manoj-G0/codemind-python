a=[0]*100
a[0]=0
a[1]=2
a[2]=2
for i in range(3,100):
    a[i]=a[i-1]+a[i-2]
n=int(input())
print(a[n])