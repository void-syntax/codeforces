#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    //solution
    int n; cin >> n;
    while (n--) {
        string a; cin >> a;
        int length = a.length();
        if (length > 10) {
            cout << a[0] << length - 2 << a[length - 1] << '\n';
        } else {
            cout << a << '\n';
        }
        
    }
    return 0;   
}