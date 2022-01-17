u,l=input().split(" ")
u=int(u)
l=int(l)

for i in range(u+1,l):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        print(i,end=" ")