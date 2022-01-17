n=int(input())
c=0
if n==1:
    print("no")
else:
    for i in range(2,n//2):
        if n%i==0:
            c+=1
    if c==0:
        print("yes")
    else:
        print("no")