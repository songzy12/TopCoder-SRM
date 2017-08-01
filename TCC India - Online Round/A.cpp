#include<vector>
using namespace std;
class ILike5 {
  public:
    int transformTheSequence(vector <int> X) {
        bool found = false;
        int num_even = 0;
        for (int i = 0; i < X.size(); ++i) {
            if (X[i] % 2 == 0) 
                num_even ++;
            if (X[i] % 5 == 0)
                found = true;
        }
        if (found)
            return num_even;
        // !found
        if (num_even > 0) 
            return num_even;
        return 1;
    }
};

// with num_even == 0