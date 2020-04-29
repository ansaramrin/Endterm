#include <iostream>
using namespace std;
int main(){
int n;
cin>>n;
int a[n][n];
for(int i=0;i<n;i++){
    for(int j=0;j<n;j++)
        cin>>a[i][j];
    

int max=0;
int maxI=0;
int maxJ=0;
for(int i=0;i<n;i++)
    if(a[i][j]>max){
        max=a[i][j];
        maxI=i;
        maxJ=j;

    }
    }
cout <<"Maximum element is:"<<max<<"with coordinates"<<maxI+1<<maxJ+1;
    
}



    return 0;
}