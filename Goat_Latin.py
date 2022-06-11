s=input().split(" ")
c=0
ch=[]
for i in s:
    c+=1
    if i[0] in 'aeiouAEIOU':
        k=i+'ma'+c*'a'
        ch.append(k)
    elif i[0] not in 'aeiouAEIOU':
        k=i[1:len(i)]+i[0]+'ma'+c*'a'
        ch.append(k)
print(*ch)
    