#include<stdio.h>
int main(){
    int i,n,sum;
    printf("숫자 입력: ");
    scanf("%d",&n);

    for(i=1;i<=9;i++){
        sum=(i*n);
        printf("%d * %d = %d\n",n,i,sum);
    }
    return 0;
}