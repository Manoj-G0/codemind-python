s=input()
c=0
m=0
for i in range(len(s)):
    if s[i] in 'aeiou':
        c+=1
    else:
        m=max(c,m)
        c=0
print(max(c,m))
    