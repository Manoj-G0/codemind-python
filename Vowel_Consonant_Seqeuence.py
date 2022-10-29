s=input()
for i in range(len(s)):
    if s[i] in 'aeiou' and (i==0 or s[i-1] not in 'aeiou'):
        print("V",end="")
    elif (i==0 or s[i-1] in 'aeiou') and s[i] not in 'aeiou':
        print("C",end="")
        