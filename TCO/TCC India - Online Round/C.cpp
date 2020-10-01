#include "bits/stdc++.h"
using namespace std;
const int N = 2005;
const int mod = 1e9 + 7;
int n;
bool pal[N][N];
int dp[N][2];
int solve(int pos , int done){
  if(pos > n){
    return done;
  }
  if(dp[pos][done] != -1){
    return dp[pos][done];
  }
  long long res = 0;
  res += solve(pos + 1 , done);
  res += solve(n + 1 , done | pal[pos][n]);
  for(int i = pos + 1 ; i <= n ; ++i){
    res += solve(i + 1 , done | pal[pos][i - 1]);
  }
  return dp[pos][done] = res % mod;
}
struct ConsecutivePalindromes{
  int countStrings(string str){
    n = str.size();
    str = " " + str;
    memset(pal , 0 , sizeof(pal));
    for(int i = 1 ; i <= n ; ++i){
      pal[i][i] = 1;
    }
    for(int i = 1 ; i < n ; ++i){
      if(str[i] == str[i + 1]){
        pal[i][i + 1] = 1;
      }
    }
    for(int siz = 3 ; siz <= n ; ++siz){
      for(int i = 1 ; i + siz - 1 <= n ; ++i){
        if(str[i] == str[i + siz - 1]){
          pal[i][i + siz - 1] = pal[i + 1][i + siz - 2];
        }
        else{
          pal[i][i + siz - 1] = 0;
        }
      }
    }
    for(int i = 1 ; i <= n ; ++i){
      pal[i][i] = 0;
    }
    for(int siz = 2 ; siz <= n ; ++siz){
      for(int i = 1 ; i + siz - 1 <= n ; ++i){
        int j = i + siz - 1;
        pal[i][j] |= pal[i][j - 1] | pal[i + 1][j];
      }
    }
    memset(dp , -1 , sizeof(dp));
    return solve(1 , 0);
  }
};