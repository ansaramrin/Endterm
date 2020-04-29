#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
int n;
cin>>n;
 vector<int> a;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        a.push_back(x);
   }
   int x,y;
   cin >> x >> y;

   reverse(a.begin()+ x,a.end() - y + 2)    ;
    for(int i = 0; i < n; ++i){
        cout << a[i] << " ";
    }

    return 0;
}