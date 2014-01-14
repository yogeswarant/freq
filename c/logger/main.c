#include <stdio.h>
#include "logger.h"

int main()
{
	int val = 0;
	printf("Printing using printf val=%d\n", val);
	eprint("Printing using eprint val=%d\n", val);
	dprint("Printing using dprint val=%d\n", val);
	return 0;
}
