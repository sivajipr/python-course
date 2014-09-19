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

    free(p);
}

main()
{
    /* call "fun" in an infinite loop */

    while(1) {
        fun();
    }

    
}
    
