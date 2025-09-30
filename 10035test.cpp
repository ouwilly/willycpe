#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    long long int a,b,d;
    

    while(cin>>a>>b){
        if (a == 0 && b == 0)break;
        long long int c=0;
        long long int e=0;
        while(a>0 || b>0 || c>0){
            d= a%10 + b%10 + c;
            if(d >= 10)
                e++;
            
            c=d/10;
            a=a/10;
            b=b/10;
        }
        if(e==0)
            cout<< "No carry operation."<<endl;
        else if(e==1)
            cout<<"1 carry operation."<<endl;
        else
            cout<<e<<" carry operations."<<endl;


    }
    return 0;
}