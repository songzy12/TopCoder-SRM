#include<algorithm>
using namespace std;

class SquareMaking {
  public:
	int getMinimalPrice(int a, int b, int c, int d) {
        int t[] = {a,b,c,d};
        sort(t, t+4);
        int ans = 0;
        for (int i = 0; i < 4; ++i)
            ans += abs(t[i]-t[2]);
        return ans;
    }
};