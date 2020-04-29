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
   int k,f;
   cin >> k >> f;
    a.insert(a.begin()+k,f);
    for(int i = 0; i < a.size(); ++i){
        cout << a[i] << " ";
    }
}