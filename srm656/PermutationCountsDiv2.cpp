#include<iostream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>

using namespace std;

const int mod = 1e9+7; 
const int MAXN = 200;
class PermutationCountsDiv2 {
    bool g[MAXN + 5];  
    int dp[MAXN + 5][MAXN + 5];  
  public:
    // N will be between 1 and 200
    int countPermutations(int N, vector <int> pos) {
        memset(g, 0, sizeof(g));
        for (int x : pos)
            g[x] = true;
        memset(dp, 0, sizeof(dp));  
        dp[1][1] = 1;  
        for (int i = 2; i <= N; i++)  
        {  
            for (int last = 1; last <= i; last++)  
            {  
                // for i numbers in total, ends with number last
                if (!g[i - 1])  
                {  
                    for (int j = last; j <= i; j++)  
                        dp[i][last] = (dp[i][last] + dp[i - 1][j]) % mod;  
                }  
                else  
                {  
                    for (int j = last - 1; j >= 1; j--)  
                        dp[i][last] = (dp[i][last] + dp[i - 1][j]) % mod;  
                }  
            }  
        }  
        int res = 0;  
        for (int i = 0; i <= N; i++)  
            res = (res + dp[N][i]) % mod;  
        return res;  
    }
};

/*
5
{3}
Returns: 9
Given that pos = {3}, we are looking for permutations where p(1) > p(2), p(2) > p(3), p(3) < p(4), and p(4) > p(5). 
*/