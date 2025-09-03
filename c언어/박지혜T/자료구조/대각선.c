#include <stdio.h>
int main(void)
{
    int n, m;
    scanf("%d %d", &n, &m);
    int arr[100][100];
    int total = 0;
    int cont = 1;
    while (cont <= n * m)
    {
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i + j == total)
                {
                    arr[j][i] = cont++;
                }
            }
        }
        total++;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%3d", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}