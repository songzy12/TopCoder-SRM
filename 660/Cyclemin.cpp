#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#define SZY
using namespace std;
// sort(res.begin(), res.end());
class Cyclemin{
	public: 
		string bestmod(string s, int k){
			vector<string> res;
			int len = s.size();
			for(int i=0; i<len; i++){
				string temp = shift(i, s);
				int j = 0;
				for(int l=0; l<len; l++){
					if(j == k) 
						break; // order matters
					if(temp[l]!='a'){
						temp[l] = 'a';
						j ++;
					}
				}
				res.push_back(temp);
			}
			sort(res.begin(), res.end());
			return res[0];
		}
	private:
		string shift(int m, string s){
			string res = "";
			int len = s.size();
			for(int i=0; i<len; i++)
				res += s[(i+m)%len];
			return res;
		}
};

/*class Cyclemin{
	public: 
		string bestmod(string s, int k){
			return bestmod_(s, k, 0, s.size()-1);
		}
	private:
		bool cmp(int m, int n, string s){
		// return shift(m) <= shift(n) ? true : false;
			int len = s.size();
			for(int i=0; i<len; i++){
				if(s[(m+i)%len] < s[(n+i)%len])
					return true;
				if(s[(m+i)%len] > s[(n+i)%len])
					return false;
			}
			return true;
		}
		bool cmp(string s, string t){
		// return s <= t 
			int len = s.size();
			for(int i=0; i<len; i++){
				if(s[i] < t[i])
					return true;
				if(s[i] > t[i])
					return false;
			}
			return true;
		}
		string shift(int m, string s){
			string res = "";
			int len = s.size();
			for(int i=0; i<len; i++)
				res += s[(i+m)%len];
			return res;
		}
		string smallest(string s){
			int min = 0;
			int len = s.size();
			for(int i = 1; i<len; i++){
				if(cmp(i, min, s))
					min = i;
			}
			return shift(min, s);
		}
		string bestmod_(string s, int k, int l, int r){
			string temp = s;
			if(l > r)
				return s;
			if(k == 0)
				return smallest(s);
			if(k >= r - l + 1){
				for(int i=l; i<=r; i++)
					temp[i] = 'a';
				return smallest(temp);
			}
			temp[l] = 'a';
			string temp1 = bestmod_(temp, k-1, l+1, r);
			string temp2 = bestmod_(s, k, l+1, r);
			if(cmp(temp1, temp2))
				return temp1;
			return temp2;
		}
};*/

int main(){
#ifdef SZY
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	string s;
	int k;
	Cyclemin c = Cyclemin();
	while(cin>>s>>k)
		cout<<c.bestmod(s, k)<<endl;
	return 0;
}