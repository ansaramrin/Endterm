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
            int x;  
        for(int i=0;i<n;i++){
            if(a[i]>mx){
                mx=a[i];
            x=i+1;
            }
            
        }
            cout<<x<<endl;







    return 0;
}