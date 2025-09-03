#include <stdio.h>
int main() {
    int N, K;
    int r = 1, c = 1;
    scanf("%d %d", &N, &K);
    for (int i = 0; i < K; i++) {
        char mv;
        scanf(" %c", &mv);
        if (mv == 'L') {
            c--;
            if (c < 1) c = N;
        } else if (mv == 'R') {
            c++;
            if (c > N) c = 1;
        } else if (mv == 'U') {
            r--;
            if (r < 1) r = N;
        } else if (mv == 'D') {
            r++;
            if (r > N) r = 1;
        }
    }
    printf("%d %d\n", r, c);
    return 0;
}
