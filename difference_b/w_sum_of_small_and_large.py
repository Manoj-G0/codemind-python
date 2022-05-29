s=input().split(" ")
k=""
sum=0
add=0
for i in s:
    k+=max(i)
    k+=min(i)
for i in range(1,len(k),+2):
    sum+=ord(k[i])
    add+=ord(k[i-1])
print(abs(sum-add))