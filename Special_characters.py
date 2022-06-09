s=input()
c=0
e=[]
o=[]
for i in range(len(s)):
    if s[i].isalnum()==False:
        c+=1
    elif s[i].isdigit():
        if int(s[i])%2==0:
            e.append(s[i])
        else:
            o.append(s[i])
if c%2==1:
    e,o=o,e
len1=len(e)
len2=len(o)
m=max(len1,len2)
a,b=0,0
for i in range(m):
    if a!=len1:
        print(e[a],end="")
        a+=1
    if b!=len2:
        print(o[b],end="")
        b+=1
    