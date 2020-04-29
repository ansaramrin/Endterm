#include <iostream>
#include <string>
using namespace std;
int main(){
string s;
cin>>s;
for(int i=1;i<s.length();i++){
  // cout << s[i] << " " << s[i - 1] << (s[i] <= s[i - 1]) << endl;
    if(s[i] - s[i-1] != 1){
      cout<<"NO";
      return 0;
    }
}
  cout <<"YES";
}