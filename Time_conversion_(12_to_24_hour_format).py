s=input()
a=0
for i in range(len(s)):
    if s[i]!=':':
        a=a*10+ord(s[i])-48
    else:
        break
if a==12 and s[6]=='A':
    print("0",end="")
    a=a-12
    print(a,end="")
    print(":",end="")
    print(s[3],end="")
    print(s[4])
elif a==12 and s[6]=='P':
    print(a,end="")
    print(":",end="")
    print(s[3],end="")
    print(s[4])
elif a<12 and s[6]=='P':
    a=a+12
    print(a,end="")
    print(":",end="")
    print(s[3],end="")
    print(s[4])
elif a<12 and s[6]=='A':
    if a>=10:
        print(a,end="")
        print(":",end="")
        print(s[3],end="")
        print(s[4])
    else:
        print("0",end="")
        print(a,end="")
        print(":",end="")
        print(s[3],end="")
        print(s[4])