#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

class CheeseRolling{
  public:
    vector<long long> waysToWin(vector <string> wins){
		_wins_ = wins;
		int n = wins.size();
		vector<long long> ans(n);
		if(n == 2){
			int a[] = {0,1};
			do{
				ans[winner(a[0],a[1])]++;
			}while(next_permutation(a, a+2));
		}else if(n == 4){
			int a[] = {0,1,2,3};
			do{
				ans[winner(winner(a[0], a[1]), winner(a[2], a[3]))]++;
			}while(next_permutation(a, a+4));
		}else if(n == 8){
			int a[] = {0,1,2,3,4,5,6,7};
			do{
				ans[winner(winner(winner(a[0],a[1]),winner(a[2],a[3])),winner(winner(a[4],a[5]),winner(a[6],a[7])))]++;
			}while(next_permutation(a, a+8));
		}else{
			int a[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
			do{
				int t1 = winner(winner(winner(a[0],a[1]),winner(a[2],a[3])),winner(winner(a[4],a[5]),winner(a[6],a[7])));
				int t2 = winner(winner(winner(a[8],a[9]),winner(a[10],a[11])),winner(winner(a[12],a[13]),winner(a[14],a[15])));
				ans[winner(t1,t2)]++;
			}while(next_permutation(a, a+16));
		}
		return ans;
	}
  private:
	vector<string> _wins_;
    int winner(int a, int b){
		return _wins_[a][b] == 'Y' ? a : b;
	}
};

int main(){
#ifdef SZY
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	string s[] = {"NYNNNNYYNYYNNYNN",
 "NNNNNNNNNYYNYYNY",
 "YYNYYNNNNYYYYYYN",
 "YYNNYYYNYNNYYYNY",
 "YYNNNYYNYYNNNNYY",
 "YYYNNNNYYNNYYNYN",
 "NYYNNYNYNYNYYYYN",
 "NYYYYNNNYYNYNYYY",
 "YYYNNNYNNYYYYNNN",
 "NNNYNYNNNNNNYYNY",
 "NNNYYYYYNYNYYYNN",
 "YYNNYNNNNYNNYNNY",
 "YNNNYNNYNNNNNYNN",
 "NNNNYYNNYNNYNNYY",
 "YYNYNNNNYYYYYNNN",
 "YNYNNYYNYNYNYNYN"};
	vector<string> wins(s, s+16);
	
	vector<long long> ans = CheeseRolling().waysToWin(wins);
	for(int i=0; i<ans.size(); ++i)
		cout<<ans[i]<<" ";
	cout<<endl;
	return 0;
}