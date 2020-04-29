#include <iostream>
using namespace std;

int s(int n){
     int sum=0;
     if(n==0) return 0;
     return sum + n%10 +s(n/10);
}

bool f(int n){
    if((s(n)%(n%10))==0) return 1;
    else return 0;
}

int main(){
    int n;
    cin>>n;
    if(f(n)==true) cout<<"Yes";
    else cout<<"No";
        
}