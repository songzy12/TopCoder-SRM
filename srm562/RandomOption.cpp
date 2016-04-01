#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
class RandomOption
{
    // dp[i][j][k]: position i is number j with state k.
    long long dp[15][15][1<<14];
    bool flag[15][15];
public:
	double getProbability(int keyCount, vector <int> badLane1, vector <int> badLane2){
		memset(dp,0,sizeof dp);
        memset(flag,false,sizeof flag);
		
        for(int i=0;i<badLane2.size();i++)
		{
			int u=badLane2[i], v=badLane1[i];
			flag[u][v]=true;
			flag[v][u]=true;
		}
		
        for(int i=0;i<keyCount;i++) 
            // the first position is number i, with i used
            dp[1][i][1<<i]=1;
        
		for(int i=1;i<keyCount;i++)
		{
			for(int j=0;j<keyCount;j++)
			{
				for(int pre=0;pre<(1<<keyCount);pre++)
				{
					for(int k=0;k<keyCount;k++)
					{
						if(flag[j][k]||(pre&(1<<k))) 
                            // if j,k not adjacent, or k has been used
                            continue;
                        // position i+1 is number k, with position i is number j
						dp[i+1][k][pre|(1<<k)] += dp[i][j][pre];					
					}
				}
			}
		}
		
		double ans=0;
		for(int i=0;i<keyCount;i++) 
            // the last position is number i, with all number used
            ans += dp[keyCount][i][(1<<keyCount)-1];
        for(int i=1;i<=keyCount;i++) 
            // all possible permutations
            ans /= i;
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