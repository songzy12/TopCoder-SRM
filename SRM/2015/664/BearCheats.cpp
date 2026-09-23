#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <vector>

using namespace std;
class BearCheats {
   public:
    string eyesight(int A, int B) {
        int count = 0;
        while (A) {
            if (A % 10 != B % 10) count += 1;
            A /= 10;
            B /= 10;
        }
        return (B || count > 1) ? "glasses" : "happy";
    }
};
int main() {
    ios::sync_with_stdio(false);
    return 0;
}