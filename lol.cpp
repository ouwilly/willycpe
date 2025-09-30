#include <iostream>
using namespace std;

int getCycleLength(int n) {
    int count = 1;
    while (n != 1) {
        if (n % 2 == 0)
            n = n / 2;
        else
            n = 3 * n + 1;
        count++;
    }
    return count;
}

int main() {
    int i, j;
    while ( cin >> i >> j) {
        int maxCycle = 0;
        int start = i, end = j;

        if (i > j) {
            start = j;
            end = i;
        }

        for (int k = start; k <= end; k++) {
            int cycle = getCycleLength(k);
            if (cycle > maxCycle)
                maxCycle = cycle;
        }

        cout << i << " " << j << " " << maxCycle << endl;
    }
    return 0;
}
