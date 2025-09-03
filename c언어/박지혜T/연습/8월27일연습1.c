#include<stdio.h>
int main(){
    int a,b;
    int tmp;
    scanf("%d %d",&a,&b);
    if (a<=b){
        tmp=b;
        b=a;
        a=tmp;
    }
    while (b != 0)
    {   
        tmp = a % b;
        a = b;         
        b = tmp;
    }
    printf("%d\n",a);
    return 0;
}