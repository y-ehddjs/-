#include<stdio.h>
int main(){
    int n,k,m,cut;
    int arr[1000];
    scanf("%d %d",&n,&m);
    for (int i = 0; i < n; i++)//배열 이니깐 0부터 시작
    {
        scanf("%d",&arr[i]);
    }
    for (int i =0; i < n - 1; i++)//배열이니깐 0 시작, 만약 <= 으로 두면 오버로 돌아감,n-1이 효율을 올려줌
    {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] < arr[j]) {
                cut = arr[i];
                arr[i] = arr[j];
                arr[j] = cut;
            }
        }
    }
    printf("%d",arr[m-1]);
    return 0;
}