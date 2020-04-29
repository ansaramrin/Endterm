#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
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
   int sum = 0;
   sort(a.begin(),a.end());
    for(int i=n-1;i>=n-k;i--){
        sum=sum+a[i];
  }
  cout<<sum;
}