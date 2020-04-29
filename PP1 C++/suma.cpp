#include <iostream>
using namespace std;
int main(){
    int n;
    int sum;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
        sum+=a[i];
    } 
    
    cout << sum << endl;

    return 0;
}