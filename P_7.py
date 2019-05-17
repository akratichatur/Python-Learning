ss=input()
s=list(ss)
print(s)
for i in range(0,len(s)-1,2):
	temp=s[i]
	s[i]=s[i+1]
	s[i+1]=temp
	
print(s)