#include <iostream>
using namespace std;
int main(){
int n,m;
cin>>n>>m;
int a[n][m];
for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
        cin>>a[i][j];
    }
}
int minIndex1=0;
int minIndex2=0;
int sum=0;
cout << "coordinates of min elements:"<< endl;
for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){
        if(a[j][i] < a[minIndex1][minIndex2]){
            minIndex1=j;
            minIndex2=i;
        }
    }
    minIndex2 = i;
    cout << minIndex1 + 1 << ";" << minIndex2 + 1 << endl; 
    sum = sum + a[minIndex1][minIndex2];
}
    cout << "Their sum:" << endl;
    cout << sum;
    return 0;
}