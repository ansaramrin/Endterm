#include <iostream> 
using namespace std; 
int count_greater(int arr[], int n) 
{ 
    int min = INT_MAX; 
    int cnt = 0; 
    for (int i = n - 1; i >= 0; i--) { 
        if (arr[i] > min) { 
            cnt++; 
        }  
        if (arr[i] <= min) { 
            min = arr[i]; 
        } 
    } 
  
    return cnt; 
} 
int main() 
{ 
    int arr[]={1,2,3,4,5}; 
    int n=sizeof(arr) / sizeof(int);
  
    cout << count_greater(arr, n) << endl; 
  
    return 0; 
} 