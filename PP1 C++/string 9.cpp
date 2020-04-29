#include <iostream>
#include <string>
using namespace std;
int main(){
    string s;
    cin>>s;
    int cnt=0;
    for(int i=0;i<s.length();i++){
        if(s[i]==97 || s[i]==101 || s[i]==105 || s[i]==111 || s[i]==117)
        cnt++;
    cout<<cnt;
    }
}