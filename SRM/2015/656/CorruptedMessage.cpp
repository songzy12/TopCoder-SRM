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
                return constructMessage(s, c);
            }
        }
        return "";
    }

   private:
    /** Checks if the string s has exactly k characters different from c. */
    bool isValid(string s, char c, int k) {
        int count = 0;
        for (char ch : s) {
            if (ch != c) count++;
        }
        return count == k;
    }

    /** Constructs a message with the same length as s, filled with character c.
     */
    string constructMessage(string s, char c) { return string(s.size(), c); }
};

int main() {
    string s = "hello";
    int k = 3;

    cout << CorruptedMessage().reconstructMessage(s, k) << endl;

    return 0;
}