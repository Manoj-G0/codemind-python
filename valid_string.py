s=input()
a=[0]*26
c=0
for i in range(len(s)):
    a[ord(s[i])-ord('a')]+=1
for i in range(26):
    if a[i]!=0:
        k=a[i]
        break
for i in range(26):
    if a[i]!=k and a[i]!=0:
        c+=1
if c==0 or c==1:
    print("Valid String")
else:
    print("Not Valid")