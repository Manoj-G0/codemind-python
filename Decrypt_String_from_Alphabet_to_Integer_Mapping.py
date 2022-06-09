s=input()
c=[]
i=0
while i<len(s):
    if i+2<len(s) and s[i+2]=='#':
        c.append(chr((ord(s[i])-ord('0'))*10+(ord(s[i+1])-ord('0'))+96))
        i+=3
    else:
        c.append(chr(ord(s[i])+48))
        i+=1
for i in range(len(c)):
    print(c[i],end="")