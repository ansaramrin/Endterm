#include <iostream>
#include <set>
using namespace std;
int main(){
string s;
cin>>s;
 string res = "YES";
    for (int i = 0; i < s.length(); i++)
        if (!((s[i] >= '0' && s[i] <= '9') || (s[i]>='A' && s[i]<='F') || (s[i]>='a' && s[i]<='f')))
        {
            res = "NO";                                                             
            break;
        }
    cout << res;
 return 0;
}