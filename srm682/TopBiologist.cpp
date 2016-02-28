#include <map>
#include <cmath>
#include <iostream>
#include <cstring>
using namespace std;

class TopBiologist {
public:
    string findShortestNewSequence(string sequence) {
        int2chr[0] = 'A';
        int2chr[1] = 'T';
        int2chr[2] = 'C';
        int2chr[3] = 'G';
        
        chr2int['A'] = 0;
        chr2int['T'] = 1;
        chr2int['C'] = 2;
        chr2int['G'] = 3;
        int len = sequence.length();
        bool m[10000];
        memset(m, false, sizeof m);
        for (int i = 1; i <= 6; ++i) {
            for (int j = 0; j + i <= len; ++j) {
                m[str2int(sequence.substr(j, i))] = true;
                //cout<<sequence.substr(j, i)<<" "<<str2int(sequence.substr(j, i))<<endl;
            }
        }
        int i = 0;
        while (m[i]) i++;
        return int2str(i);
    }
    string int2str(int num) {
        string res = "";
        if (num == 0)
            return "A";
        while (num) {
            res = int2chr[num % 4] + res;
            num /= 4;
        }
        return res;
    }
    int str2int(string str) {
        int res = 0;
        for (int i = 0; i < str.length(); ++i) {
            res += pow(4, str.length() - 1 - i) * chr2int[str[i]];
        }
        return res;
    }
    map<int, char> int2chr;
    map<char, int> chr2int;
};

int main() {
    string sequence = "ACTGACATAGCTCGTGCATAGATCGCGTCCTTGG";
    cout<<"AA: "<<TopBiologist().str2int("AA")<<endl;
    cout<<"A: "<<TopBiologist().str2int("A")<<endl;
    cout<<TopBiologist().findShortestNewSequence(sequence)<<endl;
    return 0;
}