#include <iostream>

using namespace std;
 
int Poly(string str, int n)
{
    int cnt[n];
    int v[n];
    for(int i = 0; i < n; i++)
    {
        cnt[i] = 0;
        cin >> str;
        for(int j = 0; j < str.size(); j++)
        {
            if(str[j]==str[str.size()-j-1])
            cnt[i]++;
            if(cnt[i]==str.size())            
            v[i]=19;
            else
            {
                v[i]=18;
            }
        }

    }
    for(int i = 0; i < n; i++)
    {
        if(v[i]==19)
            cout << "Yes" << endl;
        else
        {
            cout << "No" << endl;
        }
        
    }
}

int main()
{
    int n;
    cin >> n;
    string str;
    Poly(str, n);
}

