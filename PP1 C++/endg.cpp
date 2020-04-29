#include <iostream>
#include <map>
using namespace std;

int main(){
    string s;
    map<string,int> m;
     map<string,int>:: iterator ik;
    while(cin >> s){
        m[s]++;
        
    }
    map<string,int>:: iterator ik;
     for(ik = m.begin(); ik != m.end(); ++ik)
        if(it->second % 2 == 0)
            cout << it->first << endl;
    
}
