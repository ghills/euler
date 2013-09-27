#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

static const int num_chars[][10] = 
{
    //  0   1   2   3   4   5   6   7   8   9

    // ones
    {   0,  3,  3,  5,  4,  4,  3,  5,  5,  4   },

    // tens
    {   0,  4,  6,  6,  5,  5,  5,  7,  6,  6   },

    // hundreds
    {   0,  10, 10, 12, 11, 11, 10, 12, 12, 11  },

    // thousands
    {   0,  11, 11, 13, 12, 12, 11, 13, 13, 12  }
};

// 0-19 has lots of special cases, list them here
static const int first_20_table[] =
    {   0,  3,  3,  5,  4,  4,  3,  5,  5,  4,
        3,  6,  6,  8,  8,  7,  7,  9,  8,  8   };

static const int max_upper_supported = 9999;

int count_digits_for_num(int i)
{
    int posn;
    int sum;
    int lowest_two;
    assert( i <= max_upper_supported );

    //init
    posn = 0;
    sum = 0;
    lowest_two = ( i % 100 );

    //the word 'and' for numbers >100 where lowest two are not 00
    if( i > 100
            && lowest_two != 0 )
    {
        sum += 3;
    }

    //handle special cases for lowest two (like eleven, twelve ...)
    if( lowest_two < 20 )
    {
        sum += first_20_table[lowest_two];
        posn += 2;
        i /= 100;
    }

    while( i > 0 )
    {
        sum += num_chars[posn][i%10];

        i /= 10;
        posn++;
    }

    return( sum );
}


int main( int argc, char * argv[] )
{
    int i;
    int lower, upper;
    int sum;

    if( argc < 2 )
    {
        printf("Usage: %s lower [upper]\n", argv[0] );
        return( -1 );
    }

    if( argc > 2 )
    {
        //lower and upper specified
        lower = atoi(argv[1]);
        upper = atoi(argv[2]);
    }
    else
    {
        //only one number, use as upper and lower
        upper = lower = atoi(argv[1]);
    }

    // init
    sum = 0;

    if( lower < 0
            || upper < 0
            || lower > upper
            || upper > max_upper_supported )
    {
        printf("Bad range [%d,%d]\n",lower,upper);
        return( -1 );
    }

    for( i = lower; i <= upper; i++ )
    {
        sum += count_digits_for_num(i);
    }

    printf( "Total: %d\n", sum );

    return( 0 );
}
