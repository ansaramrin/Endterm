#include <iostream>

using namespace std;
int main(){
    int n;
    cin >> n;
    int a[100000];
    for(int i = 1; i <= n; i++){
        cin >> a[i];
    }
    for(int i  = 1; i <= n; i++){
        if(a[i]%2 == 1)
        cout << a[i] << " "<<ends;

    }
return 0;
}