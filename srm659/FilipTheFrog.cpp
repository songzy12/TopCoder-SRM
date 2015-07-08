#include<iostream>
#include<vector>
using namespace std;

class FilipTheFrog{
	public:
	int countReachableIslands(vector <int> positions, int L){
		return 0;
	}
};

int main(){
	FilipTheFrog t = FilipTheFrog();
	int p[] = {1,2,3};
	vector<int> positions = vector<int>(p, p+3);
	for(int i=0; i<positions.size(); i++)
		cout<<positions[i]<<" ";
	cout<<endl;
	int L = 3;
	cout<<t.countReachableIslands(positions, L)<<endl;
	return 0;
}
