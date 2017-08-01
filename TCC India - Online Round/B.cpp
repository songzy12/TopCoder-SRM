// find the longest chain, 
// return count the number of branches

// longest chain: two maps: the 

#include "bits/stdc++.h"
using namespace std;
const int N = 55;
vector < int > v[N];
int dp[N][2];
void dfs(int node){
  for(int next : v[node]){
    dfs(next);
  }
  dp[node][0] = 1;
  for(int next : v[node]){
    dp[node][0] += dp[next][1];
  }
  for(int next : v[node]){
    int res = 0;
    for(int j : v[node]){
      if(j == next){
        res += dp[j][0];
      }
      else{
        res += dp[j][1];
      }
    }
    dp[node][0] = min(dp[node][0] , res);
  }
  dp[node][1] = dp[node][0];
  for(int i = 0 ; i + 1 < v[node].size() ; ++i){
    for(int j = i + 1 ; j < v[node].size() ; ++j){
      int res = -1;
      for(int k = 0 ; k < v[node].size() ; ++k){
        if(k == i || k == j){
          res += dp[v[node][k]][0];
        }
        else{
          res += dp[v[node][k]][1];
        }
      }
      dp[node][1] = min(dp[node][1] , res);
    }
  }
}
struct TransformTheTree{
  int countCuts(vector < int > parents){
    int n = parents.size() + 1;
    for(int i = 2 ; i <= n ; ++i){
      v[parents[i - 2] + 1].emplace_back(i);
    }
    dfs(1);
    return dp[1][1] - 1;
  }
};