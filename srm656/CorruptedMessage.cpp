#include<iostream>
#include<cstring>
#include<string>
#include<vector>
using namespace std;

class CorruptedMessage{
public:
	string reconstructMessage(string s, int k){
		int number[26]={0};
		for(int i=0; i!=s.size(); i++){
			number[s[i]-'a'] += 1;
		}
		for(int i=0; i<26; i++)
			if (number[i]==s.size()-k){
				char result[50];
				memset(result, char('a'+ i), s.size());
				result[s.size()]='\0';
				return string(result);
			}
	}
};