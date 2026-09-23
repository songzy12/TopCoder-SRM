#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

class ABBA {
   public:
    string canObtain(string initial, string target) {
        int n1 = initial.size();
        int n2 = target.size();
        for (int i = 0; i < n2 - n1; i++) {
            if (target[target.size() - 1] == 'A')
                target.erase(target.end() - 1);
            else {
                target.erase(target.end() - 1);
                reverse(target.begin(), target.end());
            }
        }
        return initial == target ? "Possible" : "Impossible";
    }
};

int main() {
    string initial = "A";
    string target = "B";
    cout << ABBA().canObtain(initial, target) << endl;
    return 0;
}