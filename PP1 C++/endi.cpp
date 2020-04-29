#include <set>
#include <iostream>
using namespace std;
int factorial(int n){
    int f = 1;
    for(int i = 1; i <= n;i++)
        f*=i;
    return f;
}

int main(){
    string s;
    cin >> s;
    set<char> st;
    set<char>::iterator ik;
    for(int i =0;i < s.size();i++){
        st.insert(s[i]);
    }
    for(ik =st.begin(); ik!=st.end(); ++ik)
        cout<<*ik;

cout << endl;
    cout << factorial(st.size());
}           
