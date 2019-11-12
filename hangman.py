
def main() :
    print("Hello")
    ans="murali"
    ques = ['m','_','r','_','l','_']
    key='\0'
    flag=0
    chance=5

    print(ques)

    while chance>0 :
        print("Enter the key")
        key=input()

        for i in range(len(ans)):
            if key==ans[i] and ques[i]=='_':
                ques[i]=ans[i]
                flag=1

        key='\0'
        print(ques)

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