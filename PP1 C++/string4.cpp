#include <iostream>
#include <string>
using namespace std;
int main(){
string s;
cin>>s;
for(int i=1;i<s.length()/2;i++){
    if(s[i] != s[s.length()-i]){
        cout << "NO";
        return 0;
    }
   }
   cout << "YES";
}