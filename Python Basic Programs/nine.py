s=0
n,k=input().split(" ")
n=int(n)
k=int(k)
A=list(input().split(" "))
A1=list(map(int,A))


s+=sum(A1[0:k:1])
print(s)