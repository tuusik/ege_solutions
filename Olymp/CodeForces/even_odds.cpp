#include <iostream>
#include <cmath>
using namespace std;
// не сработало, слишком долгое решение на одном из тестов
int main() {
    long long int n, k;
    cin >> n >> k;
    n++;
    if (k <= round(n / 2)) {
        for (long long int i = 1; i < n; i += 2) {
            k--;
            if (k == 0) {
                cout << i;
                break;
            }
        }
    }
    else {
        for (long long int i = 2; i < n; i += 2) {
            k--;
            if (k == n / 2) {
                cout << i;
                break;
            }
        }
    }
    return 0;
}