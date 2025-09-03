#include<stdio.h>//최대공약수 유클리드 호재 x
int main(){
    int a,b;
    int sum;
    scanf("%d %d",&a,&b);
    for(int i = 1; i <= a; i++){
        if (a%i==0 && b%i==0){
            sum = i;
        }
    }
    printf("%d",sum);
    return 0;
}