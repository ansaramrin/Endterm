#include <iostream>

#include <sstream>

using namespace std;
int function(int a, int b){
    return a+b;
}
int main(){
    int y, z;
    cin >> y >> z;
    cout << function(y, z);
    return 0;
}