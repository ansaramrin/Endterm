#include <iostream>
using namespace std;
void checkPoint(int x1,int y1,int x2,int y2,int p1,int p2){
    if(p1 <= x2 && p1 >= x1 && p2 <= y1 && p2 >= y2)
        cout << "yes";
    else
    {
        cout << "no";
    }
    
}
int main(){
    int x1,y1,x2,y2,p1,p2;
    cin >> x1 >> y1>> x2 >> y2>>p1>>p2;
    checkPoint(x1,y1,x2,y2,p1,p2);

}