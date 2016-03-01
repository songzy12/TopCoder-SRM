#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
class RandomOption {
    long long dp[1<<14][14];
    int c[14][14];
  public:
	double getProbability(int keyCount, vector <int> badLane1, vector <int> badLane2) {
        int n = badLane1.size();
        memset(c, 0, sizeof c);
        memset(dp, 0, sizeof dp);
        
        for (int i = 0; i < n; ++i) {
            c[badLane1[i]][badLane2[i]] = 1;
            c[badLane2[i]][badLane1[i]] = 1;
        }
        
        for (int i = 0; i < keyCount; ++i)
            dp[1<<i][i] = 1;
        
        for (int k = 1; k < (1<<keyCount); ++k) {
            for (int i = 0; i < keyCount; ++i) {
                if (dp[k][i] == 0)
                    continue;
                for (int j = 0; j < keyCount; ++j) {
                    if (k & (1<<j))
                        continue;
                    if (c[i][j])
                        continue;
                    dp[k | (1<<j)][j] += dp[k][i];
                }
            }
        }
        double ans = 0;
        for (int i = 0; i < keyCount; ++i) {
            ans += dp[(1<<keyCount) - 1][i];
        }
        for (int i = 0; i < keyCount; ++i)
            ans /= i + 1;
        return ans;
	}
};

int main() {
    int keyCount = 5;
    int lane1[] = {0};
    int lane2[] = {3};
    int len = 1;
    vector<int> badLane1(lane1, lane1 + len);
    vector<int> badLane2(lane2, lane2 + len);
    cout<<RandomOption().getProbability(keyCount, badLane1, badLane2)<<endl;
	return 0;
}

/*
Examples
0)
5
{0}
{3}
Returns: 0.6
There are 5 keys and only one bad pair. The probability that these lanes are assigned to adjacent keys is 4 / (5 choose 2) = 0.4, so the probability that we have a good arrangement is 1 - 0.4 = 0.6.
1)	
5
{0, 1, 2}
{1, 2, 0}
Returns: 0.1
In a good arrangement, no two of the lanes 0, 1, and 2 may be adjacent. Hence they have to be assigned to keys 0, 2, and 4, in some order. The probability of this event is (3! * 2!) / 5! = 0.1.
2)	
5
{2, 2, 2, 2}
{0, 1, 3, 4}
Returns: 0.0
All the pairs of lane 2 and other lanes are bad, so it is impossible to obtain a good arrangement.
3)	
7
{0, 1, 2}
{6, 5, 4}
Returns: 0.3904761904761904
4)	
7
{3, 5, 1, 0, 2, 6, 4}
{0, 2, 4, 6, 1, 5, 3}
Returns: 0.09166666666666667
*/