#include<stdio.h>
int main(){
    double num1,num2,result;
    char a;
    printf("첫 번째 숫자 입력: ");
    scanf("%lf", &num1);
    printf("연산자를 입력: ");
    scanf(" %c",&a);
    printf("첫 번째 숫자 입력: ");
    scanf("%lf", &num2);
    switch(a) {
        case '+':
            result = num1 + num2;
            printf("결과: %.2lf\n", result);
            break;
        case '-':
            result = num1 - num2;
            printf("결과: %.2lf\n", result);
            break;
        case '*':
            result = num1 * num2;
            printf("결과: %.2lf\n", result);
            break;
        case '/':
            if (num2 != 0)
                result = num1 / num2;
            else {
                printf("error\n");
                return 1;
            }
            printf("결과: %.2lf\n", result);
            break;
        default:
            printf("error\n");
            return 1;
    }
    return 0;
}