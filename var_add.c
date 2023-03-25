#include <stdio.h>

int main()
{
    int a = 10;
    int *p = &a;

    // printf("%d\n", *p);
    printf("%p\n", p); // 0x7ffe60b3dc5c

    return 0;
}