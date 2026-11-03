#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Your solution here
    int t; cin >> t;
    while (t--) {
        int counter = 0;
        int a,b,c,d; cin >> a >> b >> c >> d;
        if (a < b) {
            counter += 1;
        } if (a < c) {
            counter += 1;
        } if (a < d) {
            counter += 1;
        }
        cout << counter << '\n';
    }
    return 0;
}