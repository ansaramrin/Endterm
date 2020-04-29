#include <iostream>
using namespace std;
void Foo(int a,int b,int x,int y){
 
 if(a==x || b==y || a==y|| b==x){
 cout<<"Thanks, Nurbek";
 return;
 }
 else if(a!=x || b!=y || a!=y || b!=x){
 cout<<"Impossible";
 return;
 }
} 
int main(){
    int a,b,x,y;
    cin>>a>>b>>x>>y;
    Foo(a,b,x,y);
}
