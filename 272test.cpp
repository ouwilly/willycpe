#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int check=1;
    char test;

    while(cin.get(test)){
        if (test=='"'){
            if(check==1)
                cout<<"``";
            else
                cout<<"''";
            check=(check+1)%2;
        
            
        }
        else
            cout<<test;
    }

    return 0;
}