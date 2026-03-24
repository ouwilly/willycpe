#include <iostream>
#include <stdlib.h>
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin>>T;
    while(T--){
        int r;
        cin>>r;

        int v[501]={};
        int res=0;

        for(int i=0;i<r;i++){
            cin>>v[i];
        }

        sort(v,v+r);
        int mid=v[r/2];

        for(int i=0;i<r;i++){
            res+=abs(mid-v[i]);
        }
        cout<<res<<endl;
    }
    return 0;
}