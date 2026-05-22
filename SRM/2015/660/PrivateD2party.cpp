#include<iostream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>

using namespace std;
const int MAXN = 50;

class PrivateD2party {
    
    vector<int> a, mark;
    bool dfs(int i) {
        if (mark[i] == 0) {
            if (a[i] == i)
                return false;
            mark[i] = 2; // 2 means marked in this round
            bool res = dfs(a[i]);
            mark[i] = 1;
            return res;
        } else if (mark[i] == 1) {
            return false;
        } else {
            return true;
        }
    }
  public:
    // n will be between 1 and 50
    int getsz(vector <int> a) {
        this->a = a;
        mark  = vector<int>(a.size(), 0);
        int cycle = 0;
        for (size_t i = 0; i < a.size(); ++i) {
            if (!mark[i]) 
                if (dfs(i))
                    cycle++;
        }
        return a.size() - cycle;
    }
};

/*
For each i, 
a[i] is either the number of the person disliked by friend i, 
we have a[i]=i if friend i likes everybody else
*/