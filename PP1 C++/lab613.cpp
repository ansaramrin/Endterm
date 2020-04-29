#include <iostream>
#include <map>

using namespace std;

void FOO(int n,int arr[])

    for(int i = n-1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
int n;
cin >> n;
int arr[n];
for(int i = 0; i < n; i++)
{
    cin >> arr[i];
}
FOO(n, arr);
}