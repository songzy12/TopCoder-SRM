#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

class ExactTreeEasy {
   public:
    vector<int> getTree(int n, int m) {
        vector<int> ans;
        for (int i = 0; i < n - m; ++i) {
            ans.push_back(i);
            ans.push_back(i + 1);
        }
        for (int i = n - m + 1; i < n; ++i) {
            ans.push_back(n - m);
            ans.push_back(i);
        }
        return ans;
    }
};
int main() {
    int n, m;
    ExactTreeEasy exact;
    while (cin >> n >> m) {
        vector<int> ans = exact.getTree(n, m);
        for (int i = 0; i < ans.size(); ++i) cout << ans[i] << " ";
        cout << endl;
    }
    return 0;
}