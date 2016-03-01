#include<string>
using namespace std;
class EqualSubstrings2 {
  private:
    int get(string s, int sublen) {
        int len = s.length();
        int ans = 0;
        for (int i = 0; i + sublen <= len; ++i) {
            string temp = s.substr(i, sublen);
            for (int j = i + sublen; j + sublen <= len; ++j) {
                if (temp == s.substr(j, sublen))
                    ans ++;
            }
        }
        return ans;
    }
  public:
    int get(string s) {
        int len = s.length();
        int ans = 0;
        for (int i = 1; i <= len / 2; ++i) {
            ans += get(s, i);
        }
        return ans;
    }
};