#include <stdio.h>
int main() {
    int t;
    char s[81];
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        scanf("%s", s);
        int sum = 0, cnt = 0;
        for(int j = 0; s[j]; j++) {
            if(s[j] == 'O') {
                cnt++;
                sum += cnt;
            } else {
                cnt = 0;
            }
        }
        printf("%d\n", sum);
    }
    return 0;
}
