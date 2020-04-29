#include <iostream>
#include <string>
using namespace std;
int main(){
    string s;
    char x;
    cin>>s>>x;
    int n;
    cin>>n;
    int cnt=0;
    for(int i=0;i<s.length();i++){
    if(s[i]==x)
        cnt++;
    }
    if(cnt==n)cout<<"YES";
    else cout<<"NO";
    return 0;
}