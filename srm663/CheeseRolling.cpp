#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

class CheeseRolling {
    
  public:
  inline bool bit (const int &mask, const int &pos) {
    return (mask >> pos) & 1;
  }
  
  int cnt[1 << 16];
  long long dp[1 << 16][16];
  
  public:
    vector<long long> waysToWin(vector <string> wins) {
        int n = wins.size ();
        for (int i = 0; i < n; ++i)
          dp[(1 << i)][i] = 1;
            for (int mask = 1; mask < (1 << n); ++mask) {
          cnt[mask] = __builtin_popcount (mask);
          if (__builtin_popcount (cnt[mask]) != 1)
            continue;
          for (int subm1 = mask; subm1; subm1 = (subm1 - 1) & mask) {
            if (cnt[subm1] * 2 != cnt[mask])
              continue;
                    int subm2 = mask ^ subm1;
            for (int j = 0; j < n; ++j) {
              if (!bit (subm1, j))
                continue;
              for (int k = 0; k < n; ++k) {
                if (!bit (subm2, k))
                  continue;
                if (wins[j][k] == 'Y')
                  dp[mask][j] += dp[subm1][j] * dp[subm2][k];
                else
                  dp[mask][k] += dp[subm1][j] * dp[subm2][k];
              }
            }
          }
        }
        vector <long long> ans;
        for (int i = 0; i < n; ++i) {
          ans.push_back (dp[(1 << n) - 1][i]);
        }
        return ans;
    }
};


int main(){
	vector<string> wins({"NN", "YN"});
	vector<long long> ans = CheeseRolling().waysToWin(wins);
	return 0;
}