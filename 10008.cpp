#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore(); // 忽略換行

    int cnt[26] = {0};
    string s;

    while (n--) {
        getline(cin, s);
        for (char c : s) {
            if (isalpha(c)) {
                c = toupper(c);
                cnt[c - 'A']++;
            }
        }
    }

    vector<pair<char, int>> v;
    for (int i = 0; i < 26; i++)
        if (cnt[i]) v.push_back({char('A' + i), cnt[i]});

    sort(v.begin(), v.end(), [](auto a, auto b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    });

    for (auto x : v)
        cout << x.first << " " << x.second << "\n";
}
