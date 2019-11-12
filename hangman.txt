#include<stdio.h>
#define MAX 20
void main()
{
    char ans[MAX];
 char ques[MAX];
    char key='\0';
    int flag=0,chance=5,an;
    int i;

        printf("Enter the answer:");
        for(i=0;ans[i-1]!='\n';i++)
                scanf("%c",&ans[i]);
        printf("Enter the question:(Specify '_' instead of blank spces in between a word: ");
        for(i=0;ques[i-1]!='\n';i++)
                scanf("%c",&ques[i]);
        printf("Your question is :");
            printf("%s",ques);                                                                                                                                                                                             printf("Remaining chances: %d",chance);
    while(chance>0)
    {
        printf("Enter the key :");
        scanf("%c",&key);
        printf("\n");                                                                                                                                                                                                      for(i=0;ans[i]!='\0';i++)
        {
            if(key == ans[i] && ques[i]=='_')
            {    ques[i]=ans[i]; flag=1;}

        }
        key='\0';
        printf("%s",ques);

        for(i=0;ques[i]!='\0';i++)
                if(ques[i]=='_')        {an=1; break;}

        if(an==0) {printf("You Won"); return;}

        if(flag==0) {chance--;}
        else flag=0;

        an=0;
        printf("Remaining Chances:%d\n",chance);
    }

        if(chance==0) printf("Better luck next time\n");
}
