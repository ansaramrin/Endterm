#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool isPrime(int n){
    for(int i = 2; i * i <= n;i ++)
        if(n % i == 0)
            return false;
    return true;
}
int main(){
    int cnt = 0;
int n;
cin>>n;
 vector<int> a;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        a.push_back(x);
   }
   int k;
   cin >> k;
    for(int i = 0; i < a.size();i++){
        if(a[i] > k && isPrime(a[i]) == true)
            cnt++;
    }

    cout << cnt;
        
}