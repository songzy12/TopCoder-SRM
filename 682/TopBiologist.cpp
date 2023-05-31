#include <map>
#include <cmath>
#include <iostream>
#include <cstring>
using namespace std;

class TopBiologist {
    string dna = "ACGT";
    string res = "";
    bool flag = true;
public:
    void GenerateSeq(string sequence, string newseq, int k) {
        if (k == 0) {
            if (sequence.find(newseq) == string::npos) {
                // string::npos
                res = newseq;
                flag = false;
                return;
            }
        } else {
            int len = dna.length();
            for (int i = 0; i < len; ++i)
                GenerateSeq(sequence, newseq + dna[i], k - 1);
        }
    }
    string findShortestNewSequence(string sequence) {
        int len = sequence.length();
        for (int i = 0; i < len && flag; ++i) 
            GenerateSeq(sequence, "", i + 1); // bfs
        return res;
    }
};

int main() {
    TopBiologist tb;
    cout<<tb.findShortestNewSequence("AAGATACACCGGCTTCGTG")<<endl;
    return 0;
}