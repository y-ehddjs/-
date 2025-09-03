#include <stdio.h>
int main() {
    int arr[42] = {0}, n, i, count = 0;
    for (i = 0; i < 10; i++) {
        scanf("%d", &n);
        arr[n % 42] = 1;
    }
    for (i = 0; i < 42; i++) {
        if (arr[i]) count++;
    }
    printf("%d\n", count);
    return 0;
}
