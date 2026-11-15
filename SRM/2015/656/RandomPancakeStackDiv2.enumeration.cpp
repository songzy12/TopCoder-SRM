#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

class RandomPancakeStackDiv2 {
   public:
    double expectedDeliciousness(vector<int> deliciousness) {
        int n = deliciousness.size();
        vector<int> stack(n);
        iota(stack.begin(), stack.end(), 0);

        double result = 0;
        long long totalPermutations = 0;

        do {
            result += computeDeliciousness(stack, deliciousness);
            totalPermutations++;
        } while (next_permutation(stack.begin(), stack.end()));

        return result / totalPermutations;
    }

   private:
    double computeDeliciousness(const vector<int>& stack,
                                const vector<int>& deliciousness) {
        double result = 0;
        for (int i = 0; i < stack.size(); i++) {
            if (i > 0 && stack[i] > stack[i - 1]) {
                break;
            }
            result += deliciousness[stack[i]];
        }
        return result;
    }
};

int main() {
    vector<int> d = {1, 1, 1};
    cout << RandomPancakeStackDiv2().expectedDeliciousness(d) << endl;
    return 0;
}
