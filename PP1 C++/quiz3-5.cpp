#include <iostream>
using namespace std;

void code(int a,int b,string s){
    for(int i = 0; i < a;i++){
        if(!(s[i] <= 57 && s[i] >= 48)){
            cout << "NO";
            return;
        }
    }
    if(!(s[a] == '-')){
        cout << "NO";
        return;
    }
    for(int i = a + 1; i <= a + b;i++){
    if(!(s[i] <= 57 && s[i] >= 48)){
            cout << "NO";
            return;
        }
    }

    cout << "Yes";


}

int main(){
    int a , b;
    string s;
    cin >> a >> b >> s;
    code(a,b,s);
}