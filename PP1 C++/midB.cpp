#include <iostream>
using namespace std;

int main(){


    int n,m,x;
    cin >> n >> m >> x;
    int a[n][m];
    int cnt = 0;
    for(int i = 0;i < n;i++){
        for(int j = 0; j < m;j++){
                cin >> a[i][j];

        }
    }

    for(int i = 0;i < n;i++){
        for(int j = 0; j < m;j++){
            if(a[i][j] == x){
                cnt++;
                break;
            }
        }
    }
    cout << cnt;
}