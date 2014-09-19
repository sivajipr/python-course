#include <stdlib.h>
#define LEN 10000

void fun()
{
    char *p;

    p = malloc(LEN);
    if(p == 0) {
        perror("malloc failed");
        exit(1);
    }
}

main()
{
    while(1) {
        fun();
        usleep(10); /* slow down the loop a little bit */
    }

    
}
    
