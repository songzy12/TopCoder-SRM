#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class RandomPancakeStack {
   public:
    double expectedDeliciousness(vector<int> deliciousness) {
        d = deliciousness;
        cache.assign(d.size() + 1, vector<double>(d.size() + 1));
        computed.assign(d.size() + 1, vector<bool>(d.size() + 1, false));
        return dp(d.size(), d.size());
    }

   private:
    vector<int> d;
    vector<vector<double>> cache;
    vector<vector<bool>> computed;
    /**
     * Computes the expected deliciousness of a pancake stack with the given top
     * width and remaining cakes.
     *
     * NOTE: Two implications here:
     * 1. the cakes that has width less than top width are all in cakes left.
     * 2. we will not consider the cakes with a greater width in cakes left.
     *
     * @param top_width The width of the top layer of the stack.
     * @param cakes_left The number of cakes left to place in the stack.
     * @return The expected deliciousness of the stack.
     */
    double dp(int top_width, int cakes_left) {
        if (top_width == 0) return 0;
        if (computed[top_width][cakes_left]) {
            return cache[top_width][cakes_left];
        }

        double result = 0;
        for (int width = 0; width < top_width; width++) {
            result += 1.0 / cakes_left * (d[width] + dp(width, cakes_left - 1));
        }
        computed[top_width][cakes_left] = true;
        cache[top_width][cakes_left] = result;
        return result;
    }
};

int main() {
    int d_[] = {1, 1, 1};
    vector<int> d(d_, d_ + 3);

    cout << RandomPancakeStack().expectedDeliciousness(d) << endl;

    return 0;
}