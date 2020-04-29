#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int n;
    cin >> n;
    int a[n];
    double sum = 0;
    int cnt = 0;
    for(int i = 0;i<n;i++){
        cin >> a[i];
    }
    for(int i = 0;i<n;i++){
        if( (i + 1) % 2 == 1 && a[i] % 2 == 0){
            cnt++;
            sum+=a[i];
        }
    }
    if(cnt  == 0)
    {
        cout << 0;
        return 0;
    }
   
    cout<< setprecision(6) << fixed << (sum / cnt);

}
