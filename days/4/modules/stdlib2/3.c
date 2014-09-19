#include <stdio.h>
main()
{
    FILE *fp;
    int a[] = {19, 23, 78};

    fp = fopen("dat", "w");
    fwrite(a, sizeof(a[0]), 3, fp);

}
        
    
