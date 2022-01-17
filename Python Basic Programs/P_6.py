def __isIsomorphic__(num,k):
    kDict={}
    nDict={}
    for i in range(len(k)):
        if k[i] in kDict.keys():
            if kDict[k[i]]!=num[i]:
             
                return False;
        elif num[i] in nDict.keys():
            if nDict[num[i]]!=k[i]:
               
                return False;
        else:
            kDict[k[i]]=num[i]
            nDict[num[i]]=k[i]
    return True
def main():
   
    num=input().rstrip()
    k=input().rstrip()
    a=__isIsomorphic__(num,k)
    if a==True:
        print("yes")
    else:
        print("no")
    
    

main()

