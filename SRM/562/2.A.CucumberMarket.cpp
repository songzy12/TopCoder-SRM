#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#define SZY
using namespace std;
class CucumberMarket {
   public:
    string check(vector<int> price, int budget, int k) {
        sort(price.begin(), price.end());
        int temp = 0;
        int end = max(0, int(price.size() - k));
        int begin = price.size() - 1;  // can not use size() directly
        for (int i = begin; i >= end; i--) temp += price[i];
        return temp <= budget ? "YES" : "NO";
    }
};
int main() {
#ifdef SZY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int p[] = {1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000};
    vector<int> price(p, p + 9);
    int budget = 10000, k = 9;
    cout << CucumberMarket().check(price, budget, k) << endl;
    return 0;
}