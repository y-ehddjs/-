#include <stdio.h>

int main() {
    int i, j;
    int n;
    scanf("%d",&n);

    // up
    for(i=1; i<n; i++) {
        for(j=1; j<=n-i; j++) {
            printf(" ");
        }
        for(j=1; j<=2*i-1; j++) {
            printf("*");
        }
        printf("\n");
    }

    // down
    for(i=n; i>=1; i--) {
        for(j=1; j<=n-i; j++) {
            printf(" ");
        }
        for(j=1; j<=2*i-1; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
