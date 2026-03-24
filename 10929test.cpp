#include <bits/stdc++.h>
using namespace std;

int main(){
    string n;
    while (cin>>n &&n!="0"){
        int odd=0,even=0;
        for(int i=0;i<n.length();i++){
            if (i%2==1)
                odd+=(n[i]-'0');
            if (i%2==0)
                even+=(n[i]-'0');
        }
        string var;
        var=abs(odd-even)%11==0 ? "" : " not";
        cout<<n<<" is"<<var<<" a multiple of 11."<<endl;
    }
    return  0;
}