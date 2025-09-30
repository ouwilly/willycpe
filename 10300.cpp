#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int a; // 測資數
    cin >> a;
    while (a--) {
        int b; // 農夫人數
        cin >> b;
        long long c = 0; // 總金額
        for (int d = 0; d < b; d++) {
            long long e, f, g;
            cin >> e >> f >> g;
            c += e * g; // 注意只有 e 和 g 會用到
        }
        cout << c << "\n";
    }
    return 0;
}
