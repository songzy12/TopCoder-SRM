#include<iostream>
#include<cstring>
using namespace std;

class  StringTransform {
  private:
    bool isPossible_(string s, string t) {
    	int count[26];
        memset(count, 0, sizeof count);
        for (int i = 0; i < s.size(); ++i)
            count[s[i]-'a']++;;
        
        for (int i = s.size()-1; i >= 0; --i) {
            count[s[i]-'a'] --;
            if (s[i] == t[i])
                continue;
            // then we find some char in s[:i] before to replace s[i]
            if (!count[t[i]-'a'])
                return false;
        }
        return true;
    }
  public:
    string isPossible(string s, string t) {
        return isPossible_(s, t)?"Possible":"Impossible";
    }
};