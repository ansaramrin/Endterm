#include <iostream>
#include <set>
using namespace std;
int main(){
string str;
cin>>str;
set<char> s;
set<char>::iterator it;
int cnt=0;
for(int i=0;i<str.size();i++)
s.insert(str[i]);
for(it=s.begin();it!=s.end();it++){
    if(*it>=48 && *it<=57){
    cout << *it;
    cnt++;
 }
}
 if(cnt==0)
 cout<<"NO";
}