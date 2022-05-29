s=input().split(" ")
k=""
sum=0
add=0
for i in s:
    k+=min(i)
    k+=max(i)
for i in range(len(k)):
    print(k[i],end=" ")