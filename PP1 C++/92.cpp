#include <iostream>
using namespace std;
int main(){
    int n,x;
    cin>>n>>x;
    int prev=-1;
    for(int i=0;i<n;i++){
        cin>>x;
        if(x<prev){
            cout<<"Not interesting";
        return 0;
        }
        
        prev=x;
    }

cout<<"Interesting";
return 0;
}