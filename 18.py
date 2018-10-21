l,u=input().split(" ")
l=int(l)
u=int(u)

for n in range(l+1,u):
    x=n
    s=0
    while n!=0:
        dig=n%10
        s=s+dig**3
        n=n//10
    if s==x:
        print(x,end=" ")

