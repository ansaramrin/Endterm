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
    if(find(a.begin(),a.end(),k) != a.end())
        cout << "YES";
    else
        cout << "NO";
}