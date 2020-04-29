#include <iostream>
using namespace std;
int main(){
        int n;
        cin >> n;
        int a[n][n];
        for (int i = 0; i < n;i++){
                for (int j = 0; j < n;j++){
                    cin >> a[i][j];
            }
        }
        int mx = a[0][0];
        int second = a[0][0];
        for (int i = 0; i < n;i++){
                for (int j = 0; j < n;j++){
                    if(a[i][j] > mx){
                        second = mx;
                        mx = a[i][j];
                    }
            }
        }

        
        
        cout << second;




    return 0;
}