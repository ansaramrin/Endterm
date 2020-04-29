#include <iostream>
 
using namespace std;
 
int main()
{
int n;
cin >> n;
int a[n][n];
for (int i = 0; i < n; i++) 
{
for (int j = 0; j < n; j++) 
{
cin >> a[i][j];
}
}
int sum_main = 0;
int sum_addit = 0;
for (int i = 0; i < n; i++) {
     sum_main += a[i][i]; 
     }
for (int i = 0; i < n; i++){
     sum_addit += a[i][n-1-i];
      }
cout << sum_main << endl;
cout << sum_addit << endl;

}