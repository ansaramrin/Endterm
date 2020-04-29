#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){

vector <int> a;
int n;
cin >> n;

    for(int i=0;i<n;i++){
        int curr;
        cin >> curr;
        a.push_back(curr);
        
   }
    reverse(a.begin(),a.end());

    for(int i = 0; i < n; ++i){
        cout << a[i] << " ";
    }

    return 0;
}