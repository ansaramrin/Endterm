#include <iostream>
using namespace std;
int main(){
    int n,m,x;
    cin>>n>>m>>x;
    int cnt=0;
    for(int i=0;i<n;i++){
        bool found=false;
        for(int j=0;j<m;j++){
            int k;
            cin>>k;
            if(k==x){
                found=true;
            }
        }
    }
    if(found){
        cnt++;
    }
cout<<cnt;
}

