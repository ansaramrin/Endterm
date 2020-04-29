#include <iostream>

using namespace std;

int fu(int a[],int b[],int n){

for(int i=0;i<n;i++){
    
     cout<<b[i]-a[i]<<" ";
    }

}
int main(){
    int n;
    cin >> n;
    int a[n];
    int b[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }
    for (int i = 0; i < n; i++){
            cin >> b[i];
    }
     fu(n,a,b);
    return 0;
}
