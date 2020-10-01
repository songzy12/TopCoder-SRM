#include<set>
#include<map>
#include<ctime>
#include<queue>
#include<cmath>
#include<cstdio>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#define inf 1000000000
#define ll long long 
using namespace std;
int mx=0;
map<string,bool> mp;
class Similars{
public:
	void dfs(string a,int x,int tot,bool flag) {
		if(x==0) {
			if(flag==1) {
				if(mp[a])
                    mx=max(mx,tot);
			}
			else 
                mp[a]=1;
			return;
		}
		int t=x%10;
        x/=10;
		dfs(a,x,tot,flag);
		a[t]++;
        if(a[t]=='1')
            tot++;
		dfs(a,x,tot,flag);
	}
	int maxsim(int L, int R) {
		string a="0000000000";
		for(int i=L;i<=R;i++) {
			dfs(a,i,0,1);
			dfs(a,i,0,0);
		}
		return mx;
	}
};