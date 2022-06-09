def swap(s): 
    res=0
    k=0
    c=0
    st=0
    for i in s:
        if i=='(':
            k+=1
        else:
            c+=1
    if c!=k:
        return -1
    else:
        for i in s:
            if i=='(':
                st+=1
            elif not st:
                st+=1
                res+=1
            else:
                st-=1
        return res
n=int(input())
s = input()
print(swap(s))