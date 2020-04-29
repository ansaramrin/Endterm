#include <iostream>
using namespace std;
    int a;
    int cnt=0;
     int main(){
       
        
        cin>>a;
            for(int i=0;i<a;i++){
           int b;
           cin >>b;
            
            if(b%10==7) cnt++;
            }
            cout<<cnt<<endl;
            
    return 0;
    }