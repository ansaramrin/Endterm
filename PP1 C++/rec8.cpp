#include <iostream>
using namespace std;
int res2=1;
void foo(int n,int res1,int res2){
if(n==0)
res2=res2+res1;
cout<<res2;
return;
}
int main(){
    int n;
    cin >> n;
    int res1=0;
    foo(n,res1,res2);
}

