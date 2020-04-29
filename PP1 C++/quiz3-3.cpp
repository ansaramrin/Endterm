#include <iostream>
using namespace std;
int sum = 0;
int isFav(int n){
    if(n == 0){
        return sum;
    }
    sum = sum + n % 10;
    return isFav(n / 10);
}
int main(){
    int n;
    cin >> n;
    if(isFav(n) % (n % 10) == 0){
        cout << "YES";
    }
    else{
        cout << "NO";
    }
}