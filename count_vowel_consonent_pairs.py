def isvowel(s):
    if s in 'aeiouAEIOU':
        return 1
    else:
        return 0

s=input()
i=0
j=len(s)-1
k=(i+j)//2
c=0
if(len(s)%2!=0):
    
    while(i!=k):
        if isvowel(s[i]) and (not(isvowel(s[j]))) and (s[i]!=' ' and s[j]!=' '):
            c+=1
        elif (not(isvowel(s[i])) and isvowel(s[j])) and (s[i]!=' ' and s[j]!=' '):
            c+=1
        i+=1
        j-=1
    print(c)
else:
    while(i!=k+1 and j!=k):
        if isvowel(s[i]) and (not(isvowel(s[j]))) and (s[i]!=' ' and s[j]!=' '):
            c+=1
        elif (not(isvowel(s[i])) and isvowel(s[j])) and (s[i]!=' ' and s[j]!=' '):
            c+=1
        i+=1
        j-=1
    print(c)
    