#include <set>
#include <iostream>
using namespace std;
int main(){
    string s;
    getline(cin,s); 
    set<char> st;
    set<char> st2;
    set<char>::iterator ik;
    for(int i = 0;i < s.size();i++){
        if(st.count(s[i]) == 1)
                st2.insert(s[i]);
        st.insert(s[i]);
    }
    if(s.size() == st.size())
        cout << "NO";
   
    for(ik = st2.begin(); ik!=st2.end(); ++ik)
        if(*ik >= 48 && *ik <= 57)
            cout << *ik << " ";

}