#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

#define FALSE   (0)
#define TRUE    (1)
typedef unsigned char boolean;

boolean is_prime( unsigned long n )
{
    unsigned long upper;
    unsigned long i;

    upper = (unsigned long)sqrt(n);

    for( i = 2; i <= upper; i++ )
    {
        if( ( n % i ) == 0 ) return FALSE;
    }

    return TRUE;
}

int main( int argc, char * argv[] )
{
    unsigned long test;
    unsigned int sq_base;
    unsigned int sq;
    boolean found = FALSE;

    for( test = 33; test < 10000000; test += 2 )
    {
        sq_base = 0;
        sq = 0;
        found = FALSE;
        while( !found && (sq << 1) <= test )
         {
            found = is_prime( test - (2 * sq) );
            sq_base++;
            sq = sq_base * sq_base;
         }

        if( !found )
        {
            printf("%ld could not be made.\n", test);
            break;
        }
    }

    return(0);
}
