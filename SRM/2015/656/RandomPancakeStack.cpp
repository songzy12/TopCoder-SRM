#include<iostream>
#include<cstring>
#include<string>
#include<vector>
using namespace std;

class RandomPancakeStack{
public:
    double aux(vector<int> &d, int n, int m){
        if (n == 0)
            return 0;
        double result = 0;
        for(int i = 0; i< n; i++)
            result += 1.0 / m * (d[i] + aux(d, i, m - 1));
				return result;
	}
    double expectedDeliciousness(vector <int> d){
		return aux(d, d.size(), d.size());
	}
};

int main(){
	int d_[]={1,1,1};
	vector<int> d(d_, d_+3);
	cout << RandomPancakeStackDiv2().expectedDeliciousness(d);
	//cout<<CorruptedMessage().reconstructMessage("jlmnmiunaxzywed", 13);
	return 0;
}