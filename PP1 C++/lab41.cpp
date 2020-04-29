#include <iostream>
using namespace std;
int main(){
int n;
cin>>n;
int a[n][n];
int maxI[3]={0,0,0};
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        cin>>a[i][j];
    }
}
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        if(a[i][j]>maxI[i])
        maxI[i]=a[i][j];
    }
    cout<<maxI[i];
}
}