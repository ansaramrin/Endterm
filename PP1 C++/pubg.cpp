#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int i = 0;
  while(n > i){
  i++;
  if(n >= i*i)
  {
    cout << i*i <<  " ";
  }
  }
  return 0;
}