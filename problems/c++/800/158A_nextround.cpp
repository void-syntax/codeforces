#include <bits/stdc++.h>
using namespace std;
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n, k;
    cin >> n >> k;
 
    vector<int> arr(n);
 
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
 
    int counter = 0;
    int threshold = arr[k - 1];
 
    for (int i = 0; i < n; i++) {
        if (arr[i] >= threshold && arr[i] > 0) {
            counter++;
        }
    }
 
    cout << counter << '\n';