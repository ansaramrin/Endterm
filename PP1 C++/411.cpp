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
int sum = 0;
for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
        sum = sum + a[i][j];
    }
    cout << " The sum of row number " <<  i + 1 << " is " << sum << endl;
    sum = 0;
}

for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){
        sum = sum + a[j][i];
    }
    cout << " The sum of column number " <<  i + 1 << " is " << sum << endl;
    sum = 0;
}







    return 0;
}