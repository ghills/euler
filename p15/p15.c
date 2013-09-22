#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

//GNU Multiple Precision Arithmetic Library
#include <gmp.h>

#define NODE_INVAL -1
#define PRINT_CALC_TABLE FALSE

#define indexof(i,j,col) (((i)*(col)) + (j))

#if PRINC_CALC_TABLE
static void print_node_table( mpz_t *nodes, int node_width )
{
    int i,j;
    int col = node_width;
    for( i = 0; i < node_width; i++ )
    {
        for( j = 0; j < node_width; j++ )
        {
            gmp_printf("%Zu ", nodes[indexof(i,j,col)]);
        }
        putchar('\n');
    }
}
#endif

int main( int argc, char * argv[] )
{

    int col;
    int grid_dimension;
    int i;
    int j;
    int node_width;
    mpz_t * nodes;

    // check to make sure a grid size is passed in
    if( argc < 2 
            || ( grid_dimension = atoi(argv[1]) ) <= 0 )
    {
        printf( "Usage: %s [grid dimension]\n", argv[0] );
        return( -1 );
    }

    // need dimension + 1 each way because n cells have n+1 nodes
    node_width = grid_dimension + 1;
    col = node_width;
    nodes = malloc( sizeof(mpz_t) * (node_width) * (node_width) );
    if( !nodes )
    {
        printf("Unable to allocate memory.\n");
        return(-1);
    }

    // initialize all values to invalid so we know they haven't been calculated yet
    for( i = 0; i < node_width; i++ )
    {
        for( j = 0; j < node_width; j++ )
        {
            mpz_init( nodes[indexof(i,j,col)] );
        }
    }

    // set the last node (bottom right/target destination) to 0
    // seed inital paths to that node
    mpz_set_ui(nodes[indexof(grid_dimension,grid_dimension,col)],0);
    mpz_set_ui(nodes[indexof(grid_dimension-1,grid_dimension,col)],1);
    mpz_set_ui(nodes[indexof(grid_dimension,grid_dimension-1,col)],1);

    for( i = (node_width-1); i >= 0; i-- )
    {
        for( j = (node_width-1); j >= 0; j-- )
        {
            mpz_t * this_node = &nodes[indexof(i,j,col)];

            //already set? move on
            if( ( i == grid_dimension && j == grid_dimension ) 
                    ||  ( i == grid_dimension-1 && j == grid_dimension ) 
                    ||  ( i == grid_dimension && j == grid_dimension-1 ) ) 
            {
                continue;
            }

            //account for going to the right (if not at edge)
            if( ( j + 1 ) < node_width )
            {
                mpz_add((*this_node),(*this_node),nodes[indexof(i,j+1,col)]);
            }

            //account for going down (if not at edge)
            if( ( i + 1 ) < node_width ) 
            {
                mpz_add((*this_node),(*this_node),nodes[indexof(i+1,j,col)]);
            }
        }
    }

#if PRINT_CALC_TABLE
    // print out the calculated table
    print_node_table(nodes,node_width);
    putchar('\n');
#endif

    //the table of nodes should be calculated, just look at the results at 0,0
    gmp_printf( "Total number of paths: %Zu\n", nodes[indexof(0,0,col)] );

    //cleanup
    for( i = 0; i < node_width; i++ )
    {
        for( j = 0; j < node_width; j++ )
        {
            mpz_clear( nodes[indexof(i,j,col)] );
        }
    }
    free(nodes);

    return(0);
}
