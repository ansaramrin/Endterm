#include <iostream>
#include <string>
using namespace std;

bool f(string s,int a,int b){
       if(a>=b) return 1;
       if(s[a]!=s[b]) return 0;
       return f(s,a+1,b-1);
}

int main() {
    int n,a,b;
    cin>>n;

    for(int i=0;i<n;i++){
    string s;
    cin>>s;
    a=0;
    b=s.size()-1;
    if(f(s,a,b)==true) cout<<"Yes"<<endl;
    else cout<<"No"<<endl;
    }

    return 0;
}