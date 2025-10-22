#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int a;                 // 測資數
    cin >> a;
    while (a--) {
        int b;             // 車廂數
        cin >> b;
        vector<int> c(b);  // 序列
        for (int i = 0; i < b; i++) cin >> c[i];

        int d = 0;         // 答案：逆序對數
        for (int i = 0; i < b; i++)
            for (int j = i + 1; j < b; j++)
                if (c[i] > c[j]) d++;

        cout << "Optimal train swapping takes " << d << " swaps." << endl;
    }
    return 0;
}
