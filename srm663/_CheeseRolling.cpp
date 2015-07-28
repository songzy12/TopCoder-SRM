#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;

class CheeseRolling{
  public:
    vector<long long> waysToWin(vector <string> wins){
		
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