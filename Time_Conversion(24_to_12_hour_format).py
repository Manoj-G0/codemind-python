s=input()
a=0
for i in range(len(s)):
    if s[i]!=':':
        a=a*10+ord(s[i])-48
    else:
        break
if a==0:
    print("12:00 AM")
elif a<12:
    print(s,"AM")
elif a==12:
    print(s,"PM")
elif a>12 and a<22:
    print("0",end="")
    a=a-12
    print(a,end="")
    print(":",end="")
    print(s[3],end="")
    print(s[4],"PM")
elif a>21 and a<=23:
    a=a-12
    print(a,end="")
    print(":",end="")
    print(s[3],end="")
    print(s[4],"PM")