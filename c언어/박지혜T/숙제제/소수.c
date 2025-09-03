#include<stdio.h>

int main(){
    int num, i, cnt=0, n;
    scanf("%d",&n);
    
    while (n>0)
    { 
    scanf ("%d", &num);
    cnt=0;
    for (i=2; i<num; i++) {
            if (num % i == 0)
                cnt++;
    }
 
    if ( cnt == 0 )
        printf ("YES\n");
    else 
        printf ("NO\n");
    n--;
    }
    

    return 0;
}