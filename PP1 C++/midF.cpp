#include <iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
   sort(a,a+n);
   int sum=0;
   for(int i=0;i<n-1;i++){
       sum = sum + a[i];
   }
   if(sum>a[n-1]){
       cout<<"YES";
   }
else{
    cout<<"NO";
}
       
    

}