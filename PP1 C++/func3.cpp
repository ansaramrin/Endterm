#include <iostream>
using namespace std;
int cnt = 0;
int equalCount(int a[],int b[],int n){
    for(int i = 0;i < n;i++){
        for(int j = 0;j < n;j++){
            if(a[i] == b[j])
            cnt++;
        }
    }
    return (cnt + 1) / 2;;

}
int main(){
    int n;
    cin >> n;
    int a[n];
    int b[n];
    for(int i = 0; i < n;i++){
        cin >> a[i];
    }
    for(int i = 0; i < n;i++){
        cin >> b[i];
    }
    cout << equalCount(a,b,n);

}