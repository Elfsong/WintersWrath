#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
	int number = 123456;
	char string[7];
	char tmp[7];

	int i = 0, j = 0;

	//itoa(number, string, 10);

	//将int倒序转化为了char数组
	while(number)
	{
		tmp[i] = number%10 + '0';
		i++;
		number = number/10;
	}
	tmp[i] = 0;//相当于空指针

	printf("temp=%s\n", tmp);

	--i;

	//将tmp数组逆序输出 将它翻转过来
	while(i>=0)
	{
		string[j] = tmp[i];
		j++;
		i--;
	}
	string[j] = 0;//相当于空指针

	printf("integet = %d ; string = %s \n", number, string);
	getchar();
	return 0;
}