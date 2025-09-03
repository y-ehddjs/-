#include <stdio.h>
int main() {
    char a[101];
    fgets(a, 101, stdin);
    for (int i = 0; a[i] != '\0'; i++) {
        if (a[i] != ' ' && a[i] != '\n') {
            printf("%c", a[i]);
        }
    }
    printf("\n");
    return 0;
}