a=int(input())
for i in range (a):
    b=int(input())
    if b<=150:
        p=b*0.4463
    elif b<=400:
        p=150*0.4463+(b-150)*0.4663
    else:
        p=150*0.4463+(400-150)*0.4663+(b-400)*0.5663
    print("%.2f " % p)
