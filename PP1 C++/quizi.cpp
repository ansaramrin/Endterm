#include <iostream>
using namespace std;
int main(){
    int cnt=0;
    int n;
    cin >> n;
    int h[n];
    for(int i=0;i<n;i++){
        cin>>h[i];
    }
    int limit;
    cin >> limit;
    for(int i = 0;i < n;i++){
        if(h[i] >= limit)
        cnt++;
    } 
        cout << cnt;
    
    return 0;
}