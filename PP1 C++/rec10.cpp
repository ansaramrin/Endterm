#include <iostream>
using namespace std;
int FOO(int a,int b)
{
    if(a<10)
    return a;
    b = a % 10;
    a = a / 10;
    return b + FOO(a, b);
}

int main()
{
    int a;
    cin >> a;
    int b = 0;
    cout << FOO(a, b);
}