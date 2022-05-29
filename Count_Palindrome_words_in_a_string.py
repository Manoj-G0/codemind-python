s=input()
s=s.lower()
s=s.split(' ')
k=0
for i in range(len(s)):
    temp=s[i][::-1]
    if temp==s[i]:
        k+=1
print(k)
    