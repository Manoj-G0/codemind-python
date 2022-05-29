s=input().split(" ")
k=""
for i in s:
    k+=max(i)
    k+=min(i)
for i in range(1,len(k),+2):
    print(ord(k[i-1])-ord(k[i]),end=" ")