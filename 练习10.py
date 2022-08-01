t={}
b=1
c=True
while c:
    t[b]=0
    a=list(input().split())
    if a[0]=="0":
        c=False
    else:
        for i in range(int(a[0])):
            t[b]+=int(a[i+1])
        b+=1
for i in range(1,b):
    print(t[i])
    
