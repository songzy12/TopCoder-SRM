#include<vector>
#include<algorithm>
using namespace std;
class MoveStonesEasy {
  public:
    int get(vector <int> a, vector <int> b) {
        int n = a.size();
        int na = accumulate(a.begin(), a.end(), 0);
        int nb = accumulate(b.begin(), b.end(), 0);
        if (na != nb)
            return -1;
        for (int i = 0; i < n; ++i)
            a[i] -= b[i];
        int current = 0, ans = 0;
        for (int i = 0; i < n; ++i) {
            current += a[i];
            ans += abs(current);
        }
        return ans;
    }
};