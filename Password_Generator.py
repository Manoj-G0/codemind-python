s=input().split(",")
a=[]
m=0
k=""
for i in s:
    a=i.split(":")
    name=a[0]
    num=a[1]
    m=0
    for i in num:
        if int(i)<=len(name):
            if int(i)>m:
                m=int(i)
    if m==0:
        k+='X'
    else:
        k+=name[m-1]
print(k)   