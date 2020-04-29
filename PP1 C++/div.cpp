#include <iostream>
using namespace std;
int main(){
    int i;
    int a,b,c;
    cin >> a >> b;
    c=a/b;
    for(i=1;i<=c;++i){
        if(c%i==0){
         cout << i << " ";
        }

    }
    return 0;
}