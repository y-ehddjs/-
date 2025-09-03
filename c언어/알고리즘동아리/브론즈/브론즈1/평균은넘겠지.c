#include <stdio.h>
int main() {
    int c;
    scanf("%d", &c);
    for(int i=0; i<c; i++) {
        int n, s=0, cnt=0;
        int arr[1000];
        scanf("%d", &n);
        for(int j=0; j<n; j++) {
            scanf("%d", &arr[j]);
            s += arr[j];
        }
        double avg = (double)s / n;
        for(int j=0; j<n; j++) {
            if(arr[j] > avg) cnt++;
        }
        printf("%.3f%%\n", (double)cnt/n*100);
    }
    return 0;
}
