#include <iostream>
using namespace std;
int sum = 0;
void findSum(int n){
        if(n == 0)
           return;
    sum = sum + n % 10;
    findSum(n / 10);
}
int main(){
    int n;
    cin >> n;
   findSum(n);
  cout << sum;
}