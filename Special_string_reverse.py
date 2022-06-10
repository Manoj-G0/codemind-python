k=input()
s=list(k)
a=0
b=len(s)-1
temp=""
while(a<b):
    if not s[a].isalpha():
       a+=1
    if not s[b].isalpha():
       b-=1
    else:
        
        s[a],s[b]=s[b],s[a]
        a+=1
        b-=1
for i in s:
    print(i,end="")