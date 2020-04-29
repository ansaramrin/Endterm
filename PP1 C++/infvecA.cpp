#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
int main(){
int n;
cin>>n;
 vector<int> v;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        v.push_back(x);
   }
   
   for(int i=2;i<=sqrt(n);i++)
   cout<<v[i]<<" ";
}