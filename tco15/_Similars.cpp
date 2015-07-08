#include<iostream>
#include<ctime>
using namespace std;

class Similars{
public:
	int maxsim(int L, int R){
		int result = 0, temp;
		for(int i = L; i < R; i ++)
			for(int j = i + 1; j < R + 1; j ++){
				temp = similar(i, j);
				if (temp > result)
					result = temp;
			}
		return result;
	}
	int similar(int a, int b){
		int A[10]={0}, B[10]={0};
		while(a!=0){
			A[a % 10] += 1;
			a /= 10;
		}
		while(b!=0){
			B[b % 10] += 1;
			b /= 10;
		}
		int count = 0;
		for(int i=0; i<10; i++){
			if(A[i] && B[i])
				count ++;
		}
		return count;
	}
};

int main(){
	//cout<<Similars().maxsim(12, 1021)<<endl;
	cout<<Similars().maxsim(41390, 53834)<<endl; // 5
	return 0;
}