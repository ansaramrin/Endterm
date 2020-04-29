#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>a[i][j];
        }
   cout<<endl; }
for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(a[i][j]%2==0)
           cout<<"0"<<" ";
           else{
               cout<<"1"<<" ";
           }
        }
   cout<<endl;
    }


return 0;
}