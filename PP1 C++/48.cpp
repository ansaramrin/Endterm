#include <iostream>
using namespace std;
int main(){
    int n,m;
    cin >> n >> m;
    int a[n][m];
    for(int i = 0; i < n;i++){
        for(int j = 0; j < m;j++){
        cin >> a[i][j];
    }
    }
    int minSum = 0;
    for(int j = 0; j < m;j++){
        minSum = minSum + a[0][j];
    }
    int minIndex = 0;
    int sum = 0;

      for(int i = 0; i < n;i++){
        for(int j = 0; j < m;j++){
            sum = sum + a[i][j];
    }
            if(sum < minSum){
                minIndex = i + 1 ;
                minSum = sum;
            }
            sum = 0;
    }
        cout << minIndex;

    return 0;
}