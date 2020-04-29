#include <iostream>
using namespace std;
void Foo(int a,int b,int x,int y){
    if( (x >= a && x >= b) || (y >= a && y >=b))
        cout << "Thanks, Nurbek";
    else 
        cout << "Impossible";
} 
int main(){
    int a,b,x,y;
    cin>>a>>b>>x>>y;
    Foo(a,b,x,y);
}