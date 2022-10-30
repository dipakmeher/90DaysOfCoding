// Q.10 C preprocessor Macros
#include<stdio.h>

#define MARK 120
int main(){

#if MARK <= 75
    printf("#if directive code block executed.");
#elif MARK<100
    printf("#elif directive code block executed.");
#else 
    printf("#else directive code block executed.");
#endif

return 0;
}