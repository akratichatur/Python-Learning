n=int(input())

x=n
s=0
while n!=0:
    dig=n%10
    s=s+dig**3
    n=n//10
    
if s==x:
    print("yes")
else:
    print("no")