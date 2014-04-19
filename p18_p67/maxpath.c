#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SUPPORTED_HEIGHT 500
#define TRIANGLE_NUM_CNT ( ( MAX_SUPPORTED_HEIGHT * ( MAX_SUPPORTED_HEIGHT + 1 ) ) / 2 )

#define GET_TRIANGLE_IDX( row ) ( ( ( row ) * ( ( row ) + 1 ) ) / 2 )

#define MAX(a,b) ((a < b) ? b : a)

typedef unsigned int uint;

int solve_triangle(uint * triangle, int row_count)
{
    int this_row;
    int i;

    int idx;
    int below_idx;

    for( this_row = (row_count - 2); this_row >= 0; this_row-- )
    {
        idx = GET_TRIANGLE_IDX(this_row);
        below_idx = GET_TRIANGLE_IDX(this_row + 1);

        for( i = 0; i < (this_row + 1); i++ )
        {
            triangle[idx+i] += MAX(triangle[below_idx+i], triangle[below_idx+i+1]);
        }
    }

    return triangle[0];
}

int parse_file_to_data( FILE * f, uint * triangle)
{
    char line_buf[MAX_SUPPORTED_HEIGHT * 3];
    int row_idx;
    int i;
    int base_idx;
    char * token;

    row_idx = 0;
    while(fgets(line_buf, sizeof(line_buf), f) != NULL )
    {
        base_idx = GET_TRIANGLE_IDX(row_idx);
        token = strtok(line_buf, " \n");
        triangle[base_idx] = atoi(token);
        i = 1;
        while( ( token = strtok(NULL, " \n") ) != NULL )
        {
            triangle[base_idx + i] = atoi(token);
            i++;
        }
        row_idx++;

        if( row_idx > MAX_SUPPORTED_HEIGHT )
        {
            perror("Too many rows");
            exit(-1);
        }
    }

    return row_idx;
}

int main(int argc, char * argv[])
{
    const char * fname;
    FILE * f;
    uint * triangle;
    int row_count;

    if( argc == 2 )
    {
        fname = argv[1];
    }
    else
    {
        printf("Usage: %s [input file]\n", argv[0]);
        exit(-1);
    }

    triangle = calloc( TRIANGLE_NUM_CNT, sizeof(uint) );
    if( triangle == NULL )
    {
        perror("Error allocating space for triangle data.\n");
        exit(-1);
    }

    /* read file contents into triangle buffer */
    f = fopen(fname, "r");
    if( f == NULL )
    {
        exit(-1);
    }
    row_count = parse_file_to_data(f, triangle);
    fclose(f);

    /* solve bottom up */
    printf("%d\n", solve_triangle( triangle, row_count ) );

    free(triangle);

    return 0;
}
