#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<int> fib = {1, 2};
    while (fib.back() < 100000000)
        fib.push_back(fib[fib.size() - 1] + fib[fib.size() - 2]);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << n << " = ";

        bool started = false;
        for (int i = fib.size() - 1; i >= 0; i--) {
            if (fib[i] <= n) {
                cout << "1";
                n -= fib[i];
                started = true;
            } else if (started) {
                cout << "0";
            }
        }
        cout << " (fib)" << "\n";
    }
    return 0;
}
