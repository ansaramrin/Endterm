#include <iostream>
#include <map>
using namespace std;

int main(){
        string s;
        map<string,int> m;
        while(cin >> s){
            m[s]++;  
        }
        map<string,int>:: iterator ik;
        for(ik = m.begin(); ik != m.end(); ++ik)
            if(ik->second % 2 == 0)
                cout << ik->first << endl;
                return 0;
                
}
