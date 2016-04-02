#include<iostream>
#include<algorithm>
using namespace std;

class FriendlyRobot {
public:
    int findMaximumReturns(string instructions, int changesAllowed) {
        int dp[333][333], x[333], y[333]; 
        int inf = 0x7fffffff;
        int n = instructions.size();
        x[0] = y[0] = 0;
        for (int i = 0; i < n; ++i) {
            if (instructions[i] == 'R') {
                x[i + 1] = x[i] + 1;
                y[i + 1] = y[i];
            } else if (instructions[i] == 'L') {
                x[i + 1] = x[i] - 1;
                y[i + 1] = y[i];
            } else if (instructions[i] == 'U') {
                y[i + 1] = y[i] + 1;
                x[i + 1] = x[i];
            } else if (instructions[i] == 'D') {
                y[i + 1] = y[i] - 1;
                x[i + 1] = x[i];
            }
        }
        // x[i]: position x so far
        // y[i]: position y so far
        for (int i = 0; i <= n; ++i)
            for (int j = 0; j <= changesAllowed; ++j)
                dp[i][j] = -inf;
        dp[0][0] = 0;
        // dp[i][j]: change j commands in the first i commands, the max times to O.
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= changesAllowed; ++j) {
                if (dp[i][j] != -inf) {
                    for (int k = i + 2; k <= n; k += 2) {
                        int g = (abs(x[k] - x[i]) + abs(y[k] - y[i])) >> 1;
                        // change g commands can make robot back to O again.
                        if (j + g <= changesAllowed) {
                            dp[k][j + g] = max(dp[k][j + g], dp[i][j] + 1);
                        }
                    }
                }
            }
        }
        int ans = 0;
        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j <= changesAllowed; ++j) {
                ans = max(ans, dp[i][j]);
            }
        }
        return ans;
    }
};

int main() {
    string instructions = "UULRRLLL";
    int changesAllowed = 1;
    cout<<FriendlyRobot().findMaximumReturns(instructions, changesAllowed)<<endl;
    return 0;
}