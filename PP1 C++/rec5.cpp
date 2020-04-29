#include <iostream>
using namespace std;
    void isDiv(int n){
        if(n == 1){
            cout << "YES";
            return;
        }
        if(n % 2 == 0){
            isDiv(n/2);
        }
        else{
            cout << "No";
            return;
        }
    }
int main(){
    int n;
    cin >> n;
    isDiv(n);


}