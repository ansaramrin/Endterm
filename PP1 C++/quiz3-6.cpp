#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int sum = 0;
int numD(int n){
    int cnt = 0;
    while(n > 0){
        n = n /10;
        cnt++;
    }
    return cnt;
}
int isPalindrome(int n){
        if(n == 0)
            return sum;
    sum = sum + (n % 10) * pow(10,numD(n) - 1);
    n = n / 10;
     return isPalindrome(n);
}
int main(){
    vector <int> a;
    int n;
    cin >> n;
    for(int i = 0;i < n;i++){
        int curr;
        cin >> curr;
        a.push_back(curr);
    }
     for(int i = 0;i < n;i++){
       if(isPalindrome(a[i]) == a[i])
                cout << "yes" << endl;
        else
        {
            cout << "no" << endl;
        }
        
    }

        }