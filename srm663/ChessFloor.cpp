#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

class ChessFloor{
  public: 
    int minimumChanges(vector <string> floor){
		map<char, int> m1, m2;
		int N = floor.size();
		for(int i = 0; i < N; i++)
			for(int j = 0; j < N; j++){
				if((i+j) % 2){
					m1[floor[i][j]] ++;
				}
				else{
					m2[floor[i][j]] ++;
				}
			}
		map<char, int>::iterator it;
		int max1 = 0, max2 = 0, smax1 = 0, smax2 = 0;
		char c1, c2;
		//also could brute force all the 26*26-26 combination.
		for(it = m1.begin(); it!=m1.end(); ++it){
			if(it->second > max1){
				smax1 = max1;
				max1 = it->second;
				c1 = it->first;
			}else if(it->second > smax1){
				smax1 = it->second;
			}
		}
		for(it = m2.begin(); it!=m2.end(); ++it){
			if (it->second > max2){
				smax2 = max2;
				max2 = it->second;
				c2 = it->first;
			}else if(it->second > smax2){
				smax2 = it->second;
			}
		}
		if(c1 != c2)
			return N*N-max1-max2;
		return N*N - max(max1+smax2 ,max2+smax1);
	}
};

int main(){
#ifdef SZY
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	 string s[] = {"zz", "zz"};
	vector<string> floor(s, s+2);
	cout<<ChessFloor().minimumChanges(floor)<<endl;
	return 0;
}