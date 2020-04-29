#include <iostream>
#include <vector>
using namespace std;
vector <int > a;
void toseven(int n){
    if(n == 0)
        return;
   a.push_back(n % 7);
    n = n / 7;
      toseven(n);
}

int main(){
    int n;
    cin >> n;
    toseven(n);
    reverse(a.begin(),a.end());
    for(int i = 0; i < a.size();i++){

        cout << a[i];
    }
}