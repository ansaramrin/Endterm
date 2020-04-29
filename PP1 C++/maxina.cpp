#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    int mx=-10000000;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    
        for(int i=0;i<n;i++){
            if(a[i]>mx){
                mx=a[i];
            }
        }
            cout<<mx<<endl;







    return 0;
}