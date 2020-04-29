#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int a,b,k;
    cin >> a >> b >> k;
    vector <int> v;
    for(int i = 1;i <= min(a,b);i++){
        if( a % i == 0 && b % i == 0)
            v.push_back(i);
    }
    sort(v.begin(),v.end());
    cout << v[v.size()- k];
}