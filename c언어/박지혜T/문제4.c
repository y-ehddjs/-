#include <stdio.h>

// 자리수 합 계산 함수
int digit_sum(int num) {
    int sum = 0;
    while (num != 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

// 팩토리얼 계산 함수
long long factorial(int n) {
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    int a;
    printf("정수 a 입력: ");
    scanf("%d", &a);

    int arr[a];
    int sum = 0;
    printf("%d개의 정수를 입력하세요: ", a);
    for (int i = 0; i < a; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    double avg = (double)sum / a;

    printf("\n[1] 합: %d\n", sum);
    printf("[2] 평균: %.3f\n", avg);
    printf("[3] %d의 팩토리얼: %lld\n", a, factorial(a));
    printf("[4] %d의 제곱: %d\n", a, a * a);

    printf("[5] 1부터 %d까지의 3의 배수: ", a);
    for (int i = 1; i <= a; i++) {
        if (i % 3 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");

    printf("[6] 정수 %d의 자리수 합: %d\n", a, digit_sum(a));

    return 0;
}
