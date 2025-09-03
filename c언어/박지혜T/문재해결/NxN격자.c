#include <stdio.h>
int main() {
    int N, K;
    int r = 1, c = 1;
    scanf("%d %d", &N, &K);
    for (int i = 0; i < K; i++) {
        char mv;
        scanf(" %c", &mv);
        if (mv == 'L') {
            if (c > 1) c--;
        } else if (mv == 'R') {
            if (c < N) c++;
        } else if (mv == 'U') {
            if (r > 1) r--;
        } else if (mv == 'D') {
            if (r < N) r++;
        }
    }
    printf("%d %d\n", r, c);
    return 0;
}
