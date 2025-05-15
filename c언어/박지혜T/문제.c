#include<stdio.h>
int main(){
    int cm,age;
    printf("키와 나이를 입력하세요");
    scanf("%d %d",&cm,&age);
    if (cm<=150){
        printf("입장 불가능");
    }
    else if (age<=8)
    {
        printf("입장 불가능");
    }
    
    else{
        printf("입장 가능");
    }
    return 0;
    //놀이기구 탑승객의 키가 150이하 이거나 나이가 8살이하이면 놀이기구 탑승을 금한다.
}