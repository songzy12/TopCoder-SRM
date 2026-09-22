#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

class Cyclemin {
   public:
    string bestmod(string s, int k) {
        vector<string> res;
        int len = s.size();
        for (int i = 0; i < len; i++) {
            string temp = shift(s, i);
            temp = replace(temp, k);
            res.push_back(temp);
        }
        sort(res.begin(), res.end());
        return res[0];
    }

   private:
    /** Returns the string obtained by cyclically shifting s to the left by m
     * positions. */
    string shift(string s, int positions) {
        int len = s.size();
        return s.substr(positions) + s.substr(0, positions);
    }

    /**
     * Returns the lexicographically smallest string obtainable by changing at
     * most k characters to 'a'.
     */
    string replace(string s, int k) {
        int cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            if (cnt == k) {
                break;
            }

            if (s[i] != 'a') {
                s[i] = 'a';
                cnt++;
            }
        }
        return s;
    }
};

int main() {
    string s = "aba";
    int k = 1;

    cout << Cyclemin().bestmod(s, k) << endl;

    return 0;
}