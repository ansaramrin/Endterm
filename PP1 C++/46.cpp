#include <iostream>
using namespace std;
int main(){
int n;
cin >>n;
int a[n][n];
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        cin>>a[i][j];
    }
}
   int maxPos1=0;
   int maxPos2=0;
    for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        if(a[i][j]>a[maxPos1][maxPos2]){
            maxPos1=i;
            maxPos2=j;
        }
    }
    }
    cout<<maxPos1 + 1 <<" "<<maxPos2 + 1;







    return 0;
}