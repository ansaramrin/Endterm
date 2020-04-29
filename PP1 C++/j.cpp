#include <iostream>

using namespace std;
int main(){

    int n;
    cin >> n;
    int a[5];

    for(int i = 1; i <= n; ++ i){
        cin >> a[i];
    }
    int count = 0;
    for(int i = 1; i <= n; ++ i){
        if(a[i]>0)++ count;
    
    }
    cout << count <<endl;
    return 0;
}