#include <stdio.h>
#include "main.h"

int body(struct f *myf)
{
    printf("params: %d %u %c %s\n", myf->x, myf->y, myf->c, myf->cp);
    int z = sum(myf->x, myf->y);
    return z;
}

int sum(int x, unsigned int y)
{
    unsigned int chi = x+y;
    printf("%d + %u = %u\n", x, y, chi);
    return chi;
}
