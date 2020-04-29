#include <iostream>
using namespace std;
int main(){
    int n;
    cin >>n;
    int mn=0;
    int cur=0;
    for(int i=1;i<=n;i++){
       cin >>cur; 
       if(cur<mn){
           mn=cur;
       }

    }
cout << mn;







}