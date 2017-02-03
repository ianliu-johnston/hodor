#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	int i;
	time_t t;

	srand((unsigned) time(&t));

	printf("%.02fs", (double)(rand() % 1812) / 404);
	return (0);
}
