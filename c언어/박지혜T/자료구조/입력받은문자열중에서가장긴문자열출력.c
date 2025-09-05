#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n > 10) n = 10;
    char *s[10];      
    char buf[100];    
    int max_len = 0;  
    int idx = 0;     
    for (int i = 0; i < n; i++) {
        scanf("%s", buf);
        int len = 0;
        while (buf[len] != '\0'){
            len++;
        }
        s[i] = (char *)malloc((len + 1) * sizeof(char));
        for (int j = 0; j <= len; j++){
            s[i][j] = buf[j];
        } 
        if (len > max_len) {
            max_len = len;
            idx = i;
        }
    }
    printf("%s", s[idx]);
    for (int i = 0; i < n; i++) {
        free(s[i]);
    }
    return 0;
}
