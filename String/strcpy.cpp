#include <iostream>
#include <malloc.h>
#include <assert.h>
#include <string.h>
using namespace std;

void stringcpy(char *to, const char *form)
{
	assert(to != NULL && form != NULL);
	while(*form != '\0')
	{
		*to++ = *form++;
	}
	*to = '\0';
}



int main(
{
	char *f;
	char *t;

	f = (char *)malloc(15);
	t = (char *)malloc(15);

	stringcpy(f, "hello");
	stringcpy(t, f);

	printf("%s\n",f);
	printf("%s\n",t);

	getchar();
	return 0;
}
