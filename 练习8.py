a=int(input())
t={}
for i in range(a):
    t[i]=0
    b=list(input().split())
    for o in range(1,int(b[0])+1):
        t[i]=t[i]+int(b[o])
for i in range(a):
    print(t[i])
