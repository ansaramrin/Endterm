#include <iostream>
using namespace std;


int main(){
    string s;
    int n;
    cin >> s;
    cin >> n;
    for(int i = 0; i < s.size();i++){
        if(s[i] + n <= 90)
            s[i] = s[i]  + n;
        else
        {
            s[i] = s[i] +  n - 26;
        }
        
    }

        cout << s;


}