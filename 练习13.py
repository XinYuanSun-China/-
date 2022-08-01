a=int(input())
v={}
for i in range(a):
    t=0
    v[i]=0;
    b=list(input().split())
    for o in range (1,int(b[0])+1):
        t+=int(b[o])
    if(t%5==0 and t%7==0 and t%3==0):
        v[i]=1
for i in range(a):
    if v[i]==1:
        print("YES")
    else:
        print("NO")
    
    
