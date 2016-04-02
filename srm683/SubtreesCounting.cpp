#include <bits/stdc++.h>
using namespace std;

const int N = 1e5+10;
const int md = 1e9+7;

class SubtreesCounting
{
    int ar[N];
    vector<int> e[N];
    int ans;
    int dp[N];
    int num[N];

    void ad(int x,int y)
    {
        e[x].push_back(y);
        e[y].push_back(x);
    }

    void pre(int n,int a0,int b,int c,int m)
    {
        ar[0]=a0;
        for(int i=1;i<=n-2;i++)
            ar[i]=(1LL*b*ar[i-1]+c)%m;
        for(int i=1;i<=n-1;i++)
            ad(i,ar[i-1]%i);
    }

    int f(int x,int p)
    {
        dp[x]=1;
        num[x]=1;
        for(int i=0;i<e[x].size();i++)
            if(e[x][i]!=p)
            {
                int &y=e[x][i];
                f(y,x);
                dp[x]=(1LL*dp[x]*(1+num[y])%md+1LL*num[x]*dp[y])%md;
                num[x]=1LL*num[x]*(num[y]+1)%md;
            }
        ans+=dp[x];
        ans%=md;
        return dp[x];
    }
public:
    int sumOfSizes(int n, int a0, int b, int c, int m)
    {
        pre(n,a0,b,c,m);
        f(0,-1);
        return ans;
    }
};

/*
a[i] = (b*a[i-1] + c) mod m
j = a[i-1] mod i, connect i and j
the sum of sizes of all subtrees of T
*/