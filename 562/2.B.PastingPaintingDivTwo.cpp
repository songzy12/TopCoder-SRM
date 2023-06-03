#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define SZY
class PastingPaintingDivTwo {
   public:
    long long countColors(vector<string> clipboard, int T) {
        long long ans = 0;
        int row = clipboard.size();
        int col = clipboard[0].size();
        for (int j = 0; j < col; j++) {
            int i = 0, t = 0;
            string temp = "";
            while (i + t < row && j + t < col) {
                temp += clipboard[i + t][j + t];
                t++;
            }
            ans += count(temp, T);
        }
        for (int i = 1; i < row; i++) {
            int j = 0, t = 0;
            string temp = "";
            while (i + t < row && j + t < col) {
                temp += clipboard[i + t][j + t];
                t++;
            }
            ans += count(temp, T);
        }
        return ans;
    }

   private:
    long long count(string piece, int T) {
        // cout<<piece<<endl;
        int i = 0, len = piece.size();
        for (; i < len; ++i)
            if (piece[i] != '.') break;
        if (i == len) return 0;
        // cout<<i<<endl;
        long long ans = T;
        for (int j = i + 1; j < len; j++) {
            // check whether piece[j] is painted
            int t = j;
            while (t < len && t < j + T)
                if (piece[t++] != '.') {
                    // t changed after this
                    ans++;
                    break;
                }
        }
        return ans;
    }
};
int main() {
#ifdef SZY
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    string s[] = {"..........B..........", ".........B.B.........",
                  "........B...B........", ".......B.....B.......",
                  "......B..B.B..B......", ".....B...B.B...B.....",
                  "....B...........B....", "...B...B.....B...B...",
                  "..B.....BBBBBB....B..", ".B..........BB.....B.",
                  "BBBBBBBBBBBBBBBBBBBBB"};
    int T = 1000000000;
    vector<string> clipboard(s, s + 11);
    cout << PastingPaintingDivTwo().countColors(clipboard, T) << endl;
    return 0;
}