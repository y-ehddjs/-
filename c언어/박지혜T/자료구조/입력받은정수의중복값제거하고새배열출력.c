#include<stdio.h>
#include<stdlib.h>

int main(){
    int n;
    scanf("%d",&n);
    int *p = (int*)malloc(n * sizeof(int));
    int *p2 = (int *)malloc(n * sizeof(int));
    int cnt = 0;
    for(int i = 0; i < n; i++){
        scanf("%d",&p[i]);
        int d = 0;
        for (int j = 0; j < cnt; j++) {
            if (p[i] == p2[j]) {
                d = 1;
                break;
            }
        }
        if (!d) {
            p2[cnt++] = p[i];
        }
    }
    p = (int *)realloc(p2, cnt * sizeof(int));
    for (int i = 0; i < cnt; i++) {
        printf("%d ", p2[i]);
    }
    free(p2);
    return 0;
}