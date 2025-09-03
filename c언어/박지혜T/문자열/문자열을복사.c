#include<stdio.h>
int main(void){
    int i;
    char sum[100]="1",str[100];
    scanf("%s",str);
    for(i=0; str[i]!='\0'; i++){
        sum[i]=str[i];
    }
    printf("%s",sum);
    return 0;
}