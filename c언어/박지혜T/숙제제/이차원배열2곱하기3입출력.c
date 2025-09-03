#include <stdio.h>

int main() {
    int arr[2][3];
    int sum = 0,i,j;
    printf("2행 3열의 정수를 입력하세요:");
    for(i=0;i<2;i++) {
        for(j=0;j<3;j++) {
            scanf("%d",&arr[i][j]);
            sum+=arr[i][j];
        }
    }
    printf("배열의 합: %d",sum);

    return 0;
}
