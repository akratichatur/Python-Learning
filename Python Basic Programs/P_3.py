n=int(input())

rev=0
if n%10==0:
    while n%10==0:
        print(0,end="")
        n=n//10
    if n!=0:
        while n!=0:
            r=n%10
            n=n//10
            rev=rev*10+r
        print(rev)
else:
    while n!=0:
        r=n%10
        n=n//10
        rev=rev*10+r
    print(rev)