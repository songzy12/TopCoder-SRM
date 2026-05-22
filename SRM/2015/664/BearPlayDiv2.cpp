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
class BearPlaysDiv2{
  public:
    string equalPiles(int A, int B, int C){
		int k = gcd(gcd(A,B),C);
		int temp = (A+B+C)/k;
		if(temp % 3)
			return "impossible";
		temp /= 3;
		while(temp){
			if(temp != 1 && temp % 2)
				return "impossible";
			temp /= 2;
		}
		return "possible";
	}
  private:
	int gcd(int a, int b){
		while(a != 0){
			int c = b % a;
			b = a;
			a = c;
		}
		return b;
	}
};
int main(){
	ios::sync_with_stdio(false);
	BearPlayDiv2 test;
	cout<<test.equalPiles(2,3,4)<<endl;
	return 0;
}