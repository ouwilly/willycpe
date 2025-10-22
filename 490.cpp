#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<string> a;
    string s;
    int len = 0;

    while (getline(cin, s)) {
        a.push_back(s);
        len = max(len, (int)s.size());
    }

    for (int i = 0; i < len; i++) {
        for (int j = a.size() - 1; j >= 0; j--) {
            if (i < a[j].size()) 
                cout << a[j][i];
            else 
                cout << ' ';
        }
        cout << "\n";
    }
    return 0;
}
