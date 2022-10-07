#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<map>
#include<iomanip>
#define DEBUG
using namespace std;
class BearCheats{
  public:
	string eyesight(int A, int B){
		int count = 0;
		while (A){
			if(A%10 != B%10)
				count += 1;
			A /= 10;
			B /= 10;
		}
		return (B || count > 1)?"glasses":"happy";
	}
};
int main(){
#ifdef DEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	return 0;
}