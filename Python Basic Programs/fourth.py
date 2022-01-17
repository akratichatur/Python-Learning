x = input()
l=len(x)
if l==1:
    x=ord(x)
    if (x>=65 and x<=90) or (x>=97 and x<=122):
        print("Alphabet")
    else:
        print("No")
else:
    print("No")
