n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
if sorted(a)==sorted(b):
    print("True")
else:
    print("False")