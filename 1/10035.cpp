#include <bits/stdc++.h>
using namespace std;

int main ()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    long long int a, b;

    while (cin >> a >> b) {
        if (a == 0 && b == 0)
            break;

        long long int c = 0, t = 0;

        while (a > 0 || b > 0 || c > 0) {
            int d = a % 10 + b % 10 + c;
            if (d >= 10)
                t++;

            c = d / 10;
            a = a / 10;
            b = b / 10;
        }

        if (t == 0)
            cout << "No carry operation." << endl;
        else if (t == 1)
            cout << t << " carry operation." << endl;
        else
            cout << t << " carry operations." << endl;
    }

    return 0;
}
