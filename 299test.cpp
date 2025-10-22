#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int a;
    cin >> a;

    while(a--){
        int b;
        cin>>b;
        vector<int> c(b);
        for(int i=0;i<b;i++)
            cin>>c[i];
        int d=0;
        for(int i=0;i<b;i++)
            for(int j=i+1;j<b;j++)
                if(c[i]>c[j])
                    d++;
        cout << "Optimal train swapping takes " << d << " swaps." << endl;
    }

    return 0;
}
