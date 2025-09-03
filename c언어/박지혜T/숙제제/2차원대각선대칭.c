#include <stdio.h>

int main() {
    int arr[3][3];
    int S=1,i,j;

    printf("3x3 정수 배열 입력:\n");
    for (i=0; i<3; i++) {
        for (j=0; j<3; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    for (i=0; i<3; i++) {
        for (j=0; j<i; j++) {
if (arr[j][i] != arr[i][j]) {
                S=0;
                break;
            }
        }
    }

    if (S) {
        printf("대각선을 기준으로 대칭입니다.\n");
    } else {
        printf("대각선을 기준으로 대칭이 아닙니다.\n");
    }

    return 0;
}
