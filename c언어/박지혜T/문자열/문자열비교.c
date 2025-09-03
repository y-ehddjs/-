#include<stdio.h>
int main(void){
    int i,s=1;
    char str[100],str2[100];
    scanf("%s",str);
    scanf("%s",str2);
    for(i=0; str[i]!='\0' || str2[i]!='\0'; i++){
        if (str[i]!=str2[i]){
            s=0;
            break;
        }
    }
    if(s==0){
        printf("달라 ㅇㅅㄲ야");
    }
    else if(s==1){
        printf("0");
    }
    return 0;
}