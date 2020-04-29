#include<iostream>
using namespace std;
string s;
int main(){
cin >> s;
    for(int i = 0;i < (int)s.size();i ++){
         if(s[i] >= 97 && s[i] <= 122)
         s[i] = s[i] - 97 + 65;
         else if(s[i]>=65 && s[i]<=90)
         s[i]=s[i]-65+97;
         
    }
cout << s;
return 0;
    }