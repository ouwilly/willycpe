#include <bits/stdc++.h>
using namespace std;
//Funny Encryption Method
int count1(int x) {
    int c = 0;
    while (x) {
        if (x & 1) c++;
        x >>= 1;
    }
    return c;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int b1 = count1(n);  // 十進位直接轉二進位
        int b2 = 0;          // 每個十進位數字轉二進位
        int m = n;
        while (m) {
            b2 += count1(m % 10);
            m /= 10;
        }
        cout << b1 << " " << b2 << "\n";
    }
    return 0;
}
