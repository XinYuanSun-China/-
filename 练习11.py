a=int(input())
b={}
c={}
for i in range(a):
    c[i]=0
    b=list(input().split())
    for o in range(1,int(b[0])+1):
        c[i]+=int(b[o])
for i in range(a):
    print(c[i],'\n')
        
