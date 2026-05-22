#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
#define SZY

class ABBA{
  public:
    string canObtain(string initial, string target){
		int n1 = initial.size();
		int n2 = target.size();
		for(int i=0; i<n2-n1; i++){
			if(target[target.size()-1] == 'A')
				target.erase(target.end()-1);
			else{
				target.erase(target.end()-1);
				reverse(target.begin(), target.end());
			}
		}
		return initial == target ? "Possible" : "Impossible";
	}
};

int main(){
#ifdef SZY
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	return 0;
}