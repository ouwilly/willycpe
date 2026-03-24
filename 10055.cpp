//UVa 10055 - Hashmat the brave warrior

#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long int a,b;
    while(cin>>a>>b){
        cout<<abs(b-a)<<endl;
    }
    return 0;
}