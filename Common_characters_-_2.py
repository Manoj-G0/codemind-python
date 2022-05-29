s=input()
s=s.lower()
l=s
l=l.split(" ")
k=0
ray=0
for i in range(len(s)):
    if s[i]==" ":
        ray+=1
for i in range(len(s)):
    if(s[i]!=" "):
        c=0
        for j in l:
            if s[i] in j:
                c+=1
        if c==ray+1:
            k+=1
    else:
        break
print(k)