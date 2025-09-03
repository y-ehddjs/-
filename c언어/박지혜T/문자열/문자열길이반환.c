    #include<stdio.h>
    int main(){
        int i,sum=0;
        char str[100];
        scanf("%s",str);
        for(i=0; str[i]!='\0'; i++){
            sum+=1;
        }
        printf("%d",sum);
        return 0;
    }