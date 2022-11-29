s=input()
k=""
for i in s:
    if i not in '!, .:@#$%^&*~<>':
        k+=i.lower()
if k==k[::-1]:
    print("true")
else:
    print("false")