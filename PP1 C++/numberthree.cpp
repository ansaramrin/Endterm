#include <iostream>
using namespace std;
int main(){
    int n,m,k;
    cin >> n >> m >> k;
    if(n==m && m==k && n==k){

        cout << "3";
    }
    else if(n==m || m==k|| n==k){
        cout << "2";
    }
    else if(n!=m && m!=k && n!=k){
        cout <<"0";
    }
}