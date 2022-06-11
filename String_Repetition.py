s=input()
n=int(input())
t=n//len(s)
j=n%len(s)
c=0
k=0
for i in range(j):
    if s[i]=='a':
        c+=1
for i in range(j,len(s)):
    if s[i]=='a':
        k+=1
print(c*(t+1)+k*t)
