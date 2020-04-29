#include <iostream>
using namespace std;
int function(int n,int a[],int sum){
    for(int i=0;i<n;i++){
        sum=sum+a[i];
    
    }
    return sum;
}
int main(){
    int n;
    cin>>n;
    int a[n];
    int sum=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    cout<<function(n,a,sum);
    return 0;
}