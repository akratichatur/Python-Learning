x = input()
if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
    print("Vowel")
else:
    x=ord(x)
    if (x>=0 and x<=64) or (x>=91 and x<=96) or (x>=123 and x<=127):
        print("invalid")
    else:
        print("Consonant")
