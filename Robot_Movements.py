def robo(s1,s2):
    i,j=0,0
    while(i<len(s1) and j<len(s2)):
        if s1[i]=='#':
            i+=1
        elif s2[j]=='#':
            j+=1
        elif s1[i]!=s2[j]:
            return 0
        elif s1[i]=='A' and s2[j]=='A' and i<j:
            return 0
        elif s1[i]=='B' and s2[j]=='B' and i>j:
            return 0
        else:
            i+=1
            j+=1
    return 1


s1=input()
s2=input()
if robo(s1,s2):
    print("Yes")
else:
    print("No")