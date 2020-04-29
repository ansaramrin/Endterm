#include <iostream>
#include <string>
#include <set>
using namespace std;
int main(){

    string s;
    cin >> s;
    set<char> st;
      set<char>::iterator ik;
    for(int i = 0;i < s.size();i++){
            st.insert(s[i]);
    }

     for(ik = st.begin(); ik!=st.end(); ++ik){
        if(*st.begin() >= 48 && *st.begin()<= 57){
            cout << "NO";
            return 0;
        }
        else if((*ik >= 65 &&  *ik <= 90) || (*ik >= 97 &&  *ik <= 122)){
             
        }
        else if(*ik >= 48 &&  *ik <= 57){
           
        }

        else if(*ik == '_'){
         
        }
        else{
            cout << "NO";
            return 0;
        }
     }
     cout << "YES";
        
}