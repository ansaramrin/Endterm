#include <iostream>
using namespace std;
int findPow(int result,int n){
    if(n == 0)
        return result;
    result = result  * 2;
    return findPow(result,n-1);
}
int main(){
    int result = 1;
    int n;
    cin >> n;
    cout << findPow(result,n);



}