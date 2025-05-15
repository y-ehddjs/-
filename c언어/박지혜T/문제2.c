#include <stdio.h>

int main() {
    int a, b, i;
    scanf("%d %d", &a, &b);

    for (i = a; i <= b; i++) {
        if (i % 3 == 0) {
            printf("%d ", i);
        }
    }

    return 0;
}
//a부터b까지 3의 배수 출력