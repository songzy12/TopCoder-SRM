#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class RandomPancakeStackDiv2 {
public:
    double expectedDeliciousness(vector<int> d) {
        int n = d.size();
        
        // dp[i][j] represents the probability that a stack of size j 
        // has its top pancake at index i.
        // Size of d is up to 10 in Div2, but this scales easily to O(N^2).
        vector<vector<double>> dp(n, vector<double>(n + 1, 0.0));
        
        double total_expected = 0;

        // Base case: any pancake can be the first one chosen (bottom of the stack)
        // Each of the n pancakes has an equal probability (1 / n) of being chosen first.
        for (int i = 0; i < n; i++) {
            dp[i][1] = 1.0 / n;
            total_expected += d[i] * dp[i][1];
        }

        // Iterate over the stack size j from 1 to n-1
        for (int j = 1; j < n; j++) {
            // Iterate over all possible top pancakes of index i
            for (int i = 0; i < n; i++) {
                if (dp[i][j] == 0) continue;

                // If the current stack has size j and top is i, 
                // there are (n - j) remaining unchosen pancakes.
                // Valid next pancakes must have index k < i.
                int remaining = n - j;
                for (int k = 0; k < i; k++) {
                    // Transition probability: 
                    // Out of 'remaining' unchosen pancakes, we pick pancake k.
                    // Since all unchosen pancakes are equally likely to be picked, 
                    // the probability of picking k is 1 / remaining.
                    // Wait, is it 1 / remaining? 
                    // Yes, because any of the remaining unchosen pancakes can be chosen uniformly. 
                    // If k > i, the process terminates. If k < i, it goes on top.
                    dp[k][j + 1] += dp[i][j] * (1.0 / remaining);
                }
            }
        }

        // Sum up expected contribution across all stack sizes and top pancakes
        double ans = 0;
        for (int j = 1; j <= n; j++) {
            for (int i = 0; i < n; i++) {
                ans += dp[i][j] * d[i];
            }
        }

        return ans;
    }
};

int main() {
    vector<int> d = {1, 1, 1};
    cout << RandomPancakeStackDiv2().expectedDeliciousness(d) << endl; 
    return 0;
}