#include<stdio.h>
int ucd(int a, int b){
    if (b==0){
        return a;
    }
    return ucd(b,a%b);
}
int main(){
    int a,b;
    scanf("%d %d",&a ,&b);
    printf("%d",ucd(a,b));
}