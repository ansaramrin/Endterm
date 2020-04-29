#include <iostream>
#include <string>
#include <set>
using namespace std;
int main(){
    string s;
    getline(cin,s);
    set<char> st;
    set<char>::iterator ik;
    for(int i = 0;i < s.size();i++){
            st.insert(s[i]);
    }

     for(ik = st.begin(); ik!=st.end(); ++ik){
          if(*st.begin() == '-'){

        }
        else if((*ik >= 48 && *ik <= 55)){

        }
        else{
            cout << "NO";
            return 0;
        }
     }

    cout  << "YES";




 return 0;
}