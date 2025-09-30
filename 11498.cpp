#include <bits/stdc++.h>
using namespace std;

int main() {
    int a; // 測資數
    while (cin >> a && a) {
        int b, c; // 分界點
        cin >> b >> c;
        while (a--) {
            int d, e; // 座標
            cin >> d >> e;
            if (d == b || e == c) cout << "divisa\n";
            else if (d > b && e > c) cout << "NE\n";
            else if (d < b && e > c) cout << "NO\n";
            else if (d > b && e < c) cout << "SE\n";
            else cout << "SO\n";
        }
    }
    return 0;
}
