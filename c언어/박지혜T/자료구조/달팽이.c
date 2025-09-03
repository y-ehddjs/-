#include<stdio.h>

void bingbing(int n){
    int num[n][n];
    int a=1,i=0,j=0;
    int lt=0,rt=n-1,top=0,btm=n-1;

    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            num[i][j]=0;
        }
    }
    while(lt <= rt && top <= btm){
        for(int i=lt; i<=rt; i++){
        num[top][i]=a++;
        }
        top++;

        for(int i=top; i<=btm; i++){
            num[i][rt]=a++;
        }
        rt--;

        if(top <= btm) {
            for(int i=rt; i>=lt; i--){
                num[btm][i]=a++;
            }
            btm--;
        }

        if(lt<=rt) {
            for(int i=btm; i>=top; i--){
                num[i][lt]=a++;
            }
            lt++;
        }
    }

    for(int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            printf("%3d ", num[i][j]);
        }
        printf("\n");
    }
}
int main(){
    int n;
    scanf("%d",&n);
    bingbing(n);

    return 0;
}