
def main() :
    print("Enter the Answer:")
    ans=input()
    print("Enter the Question:")
    ques1=input()
    print('\n')
    
    ques=list(ques1)
    key='\0'
    flag=0
    chance=5

    print("Your Question Is:")
    print(''.join(ques))

    while chance>0 :
        print("Enter the key")
        key=input()

        for i in range(len(ans)):
            if key==ans[i] and ques[i]=='_':
                ques[i]=ans[i]
                flag=1

        key='\0'
        print(''.join(ques))

        for i in range(len(ques)):
            if ques[i] == '_':
                an=1
                break

        if an==0 :
            print("You Won")
            return

        if flag==0 :
            chance=chance-1

        else :
            flag=0
        an=0
        print("Remaining Chances :",chance)
        

    if chance==0:
        print("Better Luck Next Time")   



main() 
