#include <iostream>
#include <malloc.h>
using namespace std;

class Obj
{
public :
    Obj(void){ cout << "  Initialization" << endl; }
    ~Obj(void){ cout << "  Destroy" << endl; }
    void Initialize(void){ cout << "  Initialization" << endl; }
    void Destroy(void){ cout << "  Destroy" << endl; }
};

void UseMallocFree(void)
{
    Obj  *a = (Obj *)malloc(sizeof(Obj));   // 申请动态内存
    a->Initialize();                        // 初始化
    //…
    a->Destroy();   // 清除工作
    free(a);        // 释放内存
}

void UseNewDelete(void)
{
    Obj  *a = new Obj;  // 申请动态内存并且初始化
    //…
    delete a;           // 清除并且释放内存
}

int main(void)
{
	cout << "Use Malloc-Free Method:" << endl;
	UseMallocFree();
	cout << endl;
	cout << "Use New-Delete Method:" << endl;
	UseNewDelete();

	getchar();
	return 0;
}