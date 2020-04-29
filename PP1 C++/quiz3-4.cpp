#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int i = 1;
    int cnt = 0;
    while( n >= 0){
        n = n - i;
        cnt++;
        if(n <= 0)
            break;
        n = n - i * 2;
        cnt++;
        i = i + 1;
    }
    if(cnt % 2 == 0)
        cout << "Nelson";
    else
    {
        cout << "Bob";
    }
    
}

