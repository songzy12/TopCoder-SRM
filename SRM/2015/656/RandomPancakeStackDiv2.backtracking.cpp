#include <iostream>
#include <vector>

using namespace std;

class RandomPancakeStackDiv2 {
public:
    double expectedDeliciousness(vector<int> deliciousness) {
        int n = deliciousness.size();
        vector<bool> visited(n, false);
        double totalExpected = 0;

        // Start backtracking:
        // last_idx = -1 (no pancake on stack yet)
        // count_visited = 0
        // current_prob = 1.0 (probability of reaching the start is 1.0)
        // current_score = 0
        dfs(-1, 0, 1.0, 0.0, deliciousness, visited, totalExpected);

        return totalExpected;
    }

private:
    void dfs(int last_idx, int count_visited, double current_prob, double current_score,
             const vector<int>& deliciousness, vector<bool>& visited, double& totalExpected) {
        int n = deliciousness.size();
        int remaining = n - count_visited;

        // If no pancakes remain, accumulate the score for this completed path
        if (remaining == 0) {
            totalExpected += current_prob * current_score;
            return;
        }

        // Each remaining pancake is chosen uniformly at random with probability 1 / remaining
        double choiceProb = current_prob / remaining;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                // Check the game termination condition:
                // If a pancake has a greater index (width) than the top of the stack, 
                // Charlie terminates without taking it.
                if (last_idx != -1 && i > last_idx) {
                    // Early stopping: this branch ends here. 
                    // Add the score accumulated up to this point.
                    totalExpected += choiceProb * current_score;
                } else {
                    // Valid choice: take the pancake and continue
                    visited[i] = true;
                    dfs(i, count_visited + 1, choiceProb, current_score + deliciousness[i],
                        deliciousness, visited, totalExpected);
                    visited[i] = false; // Backtrack
                }
            }
        }
    }
};

int main() {
    vector<int> d = {1, 1, 1};
    cout << RandomPancakeStackDiv2().expectedDeliciousness(d) << endl; // Should output 1.66667
    return 0;
}