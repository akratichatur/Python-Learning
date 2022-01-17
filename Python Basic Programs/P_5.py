def change(st):
    s=0
    d={'X':10,'V':5,'I':1}

    for i in range(len(st)):
        if i==0:
            s=s+d[st[i]]
        else:
            if st[i]=='X':
                s=s+10
                if st[i-1]=='I':
                    s=s-2

            elif st[i]=='V':
                s=s+5
                if st[i-1]=='I':
                    s=s-2
            elif st[i]=='I':
                s=s+1
    return (s)
    
n=input()
print(change(n))