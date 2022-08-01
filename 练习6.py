a=str(input())
b=a.find(" ")
n=int(a[:b])
print(a[b+1:n+b+1])
