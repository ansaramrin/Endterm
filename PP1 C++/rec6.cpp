#include <iostream>
using namespace std;
int cnt = 0;
int countEven(string s){
    if(s.length() == 0)
        return cnt;
    if((s[s.length() - 1] - 48) % 2 == 0){
        cnt++;
    }
    return countEven(s.substr(0,s.length() - 1));

}
int main(){
    string s;
    cin >> s;
    cout << countEven(s);
}