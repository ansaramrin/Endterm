#include <iostream>
#include <string>
using namespace std;
int main(){
    string s;
    cin>>s;
    char x=s[0];
    for(int i=1;i<s.length();i++){
        x=max(x,s[i]);
    
    }
    cout<<x;
    return 0;
}