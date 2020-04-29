#include <set>
#include <iostream>
using namespace std;
int fac(int n){
    int f = 1;
    for(int i = 1; i <= n;i++)
        f*=i;
    return f;
}

int main(){
    string str;
    cin >> str;
    set<char> st;
    set<char>::iterator ik;
    for(int i =0;i < str.size();i++){
        st.insert(s[i]);
    }
    for(ik =st.begin(); ik!=st.end(); ++ik)
        cout<<*ik;

cout << endl;
    cout << fac(st.size());
}
