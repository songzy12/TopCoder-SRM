#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class CorruptedMessage {
   public:
    string reconstructMessage(string s, int k) {
        for (char c = 'a'; c <= 'z'; c++) {
            if (isValid(s, c, k)) {
                return string(s.size(), c);
            }
        }
        return "";
    }

   private:
    bool isValid(string s, char c, int k) {
        int count = 0;
        for (char ch : s) {
            if (ch != c) count++;
        }
        return count == k;
    }
};

int main() {
    string s = "hello";
    int k = 3;

    cout << CorruptedMessage().reconstructMessage(s, k) << endl;

    return 0;
}