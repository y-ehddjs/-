#include<stdio.h>
int main(void){
    char str[6]="Hello";
    int i;
    for(i=6; i>=0; i--){
        printf("%c",str[i]);
    }
    return 0;
}