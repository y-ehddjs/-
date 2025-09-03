    #include<stdio.h>
    int main(){
        int i,s=0,t=0;
        char str[100],str2[100],sum[100];
        scanf("%s",str);
        scanf("%s",str2);
        for(i=0; str[i]!='\0'; i++){
            sum[i]=str[i];
            s+=1;
        }
        for(i=0;str2[i]!='\0'; i++){
            t+=1;
        }
        for(i=0; i<=t; i++){
            sum[s+i]=str2[i];
        }
        printf("%s",sum);
        return 0;
    }