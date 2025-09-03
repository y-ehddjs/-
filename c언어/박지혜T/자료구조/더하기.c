#include <stdio.h>
int main(void)
{
    char str[100];
    scanf("%s", str);
    int sum = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == ',')
            continue;
        sum += str[i] - 48;
    }
    printf("%d", sum);
    return 0;
}