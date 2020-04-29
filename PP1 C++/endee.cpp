#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int x;
    cin >> x;
    for (int i = 0; i < x; i++)
    {   
        for(int j = 0; j < x; j++)
        {
            cout << abs(i - j) + 1 << " ";
        }
        cout  <<  endl;
    }
        
    
}
