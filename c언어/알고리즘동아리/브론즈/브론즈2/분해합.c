#include <stdio.h>
int main() {
    int n, i, j, x, sum, ans = 0;
    scanf("%d", &n);
    for(i = 1; i < n; i++) {
        x = i;
        sum = i;
        while(x > 0) {
            sum += x % 10;
            x /= 10;
        }
        if(sum == n) {
            ans = i;
            break;
        }
    }
    printf("%d\n", ans);
    return 0;
}
