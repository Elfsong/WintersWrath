#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
int main( void )
{
    FILE *fp;
    
    fp = fopen( "test.txt", "w" ); //以可写的方式打开一个文件，如果不存在就创建一个同名文件
    assert( fp );                  //所以这里不会出错
    fclose( fp );
    
    fp = fopen( "noexitfile.txt", "r" ); //以只读的方式打开一个文件，如果不存在就打开文件失败
    assert( fp );                        //所以这里出错
    fclose( fp );                        //程序永远都执行不到这里来
    return 0;
}