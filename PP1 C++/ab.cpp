#include <iostream>
using namespace std;
int main(){
int a,b;
cin >> a >> b;
if(b>a || a==b){
    cout << a << " "<< b;
}
else{
    int x,y;
    x=a;
    y=b;
    b=x;
    a=y;
    cout << a << " " << b;
}
return 0;
}