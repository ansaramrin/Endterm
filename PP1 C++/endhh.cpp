#include <iostream>
using namespace std;
int main(){

    string s;
    while(cin >> s){
        for(int i = 0;i < s.size();i++){
            if(s[i] >=  65 && s[i] <= 90)
                s[i] = s[i] + 32;
            else
                s[i] = s[i] - 32;
    }
        cout << s << endl;


}
}