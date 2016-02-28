#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
class RandomOption {
  public:
	double getProbability(int keyCount, vector <int> badLane1, vector <int> badLane2) {
        
        return 0;
	}
};

int main() {
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
    int keyCount = 3;
    int lane1[] = {0};
    int lane2[] = {3};
    int len = 1;
    vector<int> badLane1(lane1, lane1 + len);
    vector<int> badLane2(lane2, lane2 + len);
    cout<<RandomOption().getProbability(keyCount, badLane1, badLane2)<<endl;
	return 0;
}