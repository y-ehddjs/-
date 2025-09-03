#include <stdio.h>

int main(void) {
    int arr[3][3];
    int i,j;

    printf("3x3 정수 배열 입력:\n");
    for(i=0;i<3;i++) {
        for(j=0;j<3;j++) {
            scanf("%d",&arr[i][j]);
        }
    }

    printf("배열 뒤집기:\n");
    for(i=2;i>=0;i--) {
        for(j=2;j>=0;j--) {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
