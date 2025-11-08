#include<iostream>
#include<cstdio>
using namespace std;
#define SZY
class Hexspeak{
  public:
	string decode(long long ciphertext){
		string ans = "";
		bool succeed = true;
		while(ciphertext){
			int temp = ciphertext % 16;
			ciphertext /= 16;
			if(temp == 0)
				ans = "O" + ans;
			else if (temp == 1)
				ans = "I" + ans;
			else if (9 < temp && temp < 16)
				ans = char('A' + temp - 10) + ans;
			else{
				succeed = false;
				break;
			}
		}
		return succeed ? ans : "Error!";
	}
};
int main(){
#ifdef SZY
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	long long ciphertext;
	Hexspeak hex;
	while(cin>>ciphertext)
		cout<<hex.decode(ciphertext)<<endl;
	return 0;
}