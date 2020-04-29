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
   int k;
   cin>>k;
   sort(a.begin(),a.end());
   for(int i = 0; i < k; ++i){
        cout << a[i] << " ";
    }
}