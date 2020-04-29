#include <iostream>

using namespace std;
int main(){
    int A,B,C,D;
    cin >> A>>B>>C>>D;

    int a, b,c,d;

    int dollar, cent;

    a=A*10;
    b=B*25;
    c=C*5;
    d=D*100;

    dollar=(a+b+c+d)/100;
    cent=(a+b+c+d)%100;

    cout<< dollar<< " "<< cent<< endl;

    return 0;


    
}