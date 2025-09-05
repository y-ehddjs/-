    #include<stdio.h>//최대15
    #include<stdlib.h>

    int main(){
        int n;
        scanf("%d",&n);
        int *p = (int *)malloc(n * sizeof(int));
        int cnt = 0;
        for (int i =0; i < n; i++){
            int tmp;
            scanf("%d",&tmp);
            if(tmp%2==0){
                p[cnt]=tmp;
                cnt++;
            }
        }
        p = (int*)realloc(p, cnt * sizeof(int));
        for(int i = 0; i < cnt; i++){
            printf("%d ",p[i]);
        }
        free(p);
        return 0;
}
