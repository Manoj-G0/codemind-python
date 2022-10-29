s1=input().lower()
s2=input().lower()
s3=""
for i in s1:
    if i in s2 and i!=' ':
        s3+=i
if len(s3)!=0:
    print(''.join(sorted(set(s3))))
else:
    print(-1)
