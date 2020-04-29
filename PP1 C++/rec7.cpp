#include <iostream>
using namespace std;
int result = 1;
int factorial(int n){
        if(n == 0)
            return result;
        result = result * n;
        return factorial(n -1);
}
int main(){
    int n;
    cin >> n;
    cout << factorial(n);

}