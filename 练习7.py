p={}
a=int(input())
for i in range(a):
    b,c=map(str,input().split())
    if (c in b)==True:
        p[i]=1
    else:
        p[i]=0
for i in range(a):
    if p[i]==1:
        print("Found!")
    else:
        print("not Found!")
