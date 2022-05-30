def minSwaps(nums):
    #Code here
    temp=nums.copy()
    temp.sort()
    if(temp==nums):
     return 0
    c=0
    for i in range(len(nums)):
     if(temp[i]!=nums[i]):
         c+=1
         a=nums.index(temp[i])
         nums[i],nums[a]=nums[a],nums[i]
    
    return c

n=int(input())
nums=list(map(int,input().split()))
k=minSwaps(nums)
print(k)