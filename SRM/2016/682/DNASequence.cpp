#include <iostream>
using namespace std;
class DNASequence {
public:
    int longestDNASequence(string sequence) {
        int ans = 0, temp = 0;
        for (size_t i = 0; i < sequence.size(); ++i) {
            if (sequence[i] == 'A' || sequence[i] == 'C' || sequence[i] == 'G' || sequence[i] == 'T') {
                temp ++;
            } else {
                if (temp > ans)
                    ans = temp;
                temp = 0;
            }
        }
        if (temp > ans)
            ans = temp;
        return ans;
    }
};