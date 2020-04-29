#include <iostream>
#include <cmath>
using namespace std;
int main(){
int x1,y1,x2,y2;
cin>>x1>>y1>>x2>>y2;
int len=sqrt((x2-x1)*(x2-x1));
int x3,y3,x4,y4=0;
y4=y1-len;
x4=x1;
y3=y2-len;
x3=x2;
cout<<x3<<" "<<y3<<" "<<x4<<" "<<y4;


}