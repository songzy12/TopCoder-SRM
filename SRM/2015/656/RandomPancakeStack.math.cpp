#include <iostream>
#include <vector>

using namespace std;

class RandomPancakeStackDiv2 {
public:
    double expectedDeliciousness(vector<int> deliciousness) {
        int n = deliciousness.size();
        double total_expected = 0;

        // Precompute factorial(n) since it's constant for all i and r
        double fact_n = factorial(n);

        // Sum over each pancake i
        for (int i = 0; i < n; i++) {
            int cnt_larger = n - i - 1; // Number of pancakes larger than i
            double p_i = 0;

            // Sum over all possible number of preceding pancakes r
            for (int r = 0; r <= cnt_larger; r++) {
                double comb = combination(cnt_larger, r);
                double fact_rem = factorial(n - r - 1);
                
                // Add the probability term for this r
                p_i += (comb * fact_rem) / fact_n;
            }

            // E[Total] = sum of (deliciousness[i] * P_i)
            total_expected += deliciousness[i] * p_i;
        }

        return total_expected;
    }

private:
    double factorial(int n) {
        double res = 1;
        for (int i = 2; i <= n; i++) {
            res *= i;
        }
        return res;
    }

    double combination(int n, int k) {
        if (k < 0 || k > n) return 0;
        if (k == 0 || k == n) return 1;
        if (k > n - k) k = n - k; // Use symmetry of combinations
        
        double res = 1;
        for (int i = 1; i <= k; i++) {
            res = res * (n - i + 1) / i;
        }
        return res;
    }
};

int main() {
    vector<int> d = {1, 1, 1};
    cout << RandomPancakeStackDiv2().expectedDeliciousness(d) << endl; 
    return 0;
}