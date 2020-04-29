#include <iostream>
using namespace std;
int main(){
int n;
cin>>n;
int a[n];
for(int i=0;i<n;i++){
    cin>>a[i];
    }
int mx=0;
for(int i=0;i<n;i++){
   if(a[i]>mx){
       mx=a[i];
   }

}
cout<<mx << "  ";
int mn=a[0];
for(int i=0;i<n;i++){
    if(a[i]<mn){
        mn =a[i];
    }
    
}
cout<<mn;
return 0;
}