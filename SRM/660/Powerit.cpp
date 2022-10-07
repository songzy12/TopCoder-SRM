#include<iostream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>

using namespace std;

class Powerit {
    
    long get_ith_element(int i, int k, int m) {  
        // calculate i ^ (2^k - 1) in O(k) time:  
        long p = i;  
        long q = p;  
        for (int j = 1; j < k; j++) {  
            q = (q * q) % m;  
            p = (p * q) % m;  
        }  
        return p;  
    }    
    
  public:
    int calc(int n, int k, int m) {  
        // modified Sieve of Erathostenes, when the number is composite,   
        // first_factor[i] will return a prime number that divides it.  
        vector<int> first_factor(n + 1, 1);  
        for (int i = 2; i <= n; i++) {  
            if (first_factor[i] == 1) {  
                // prime  
                first_factor[i] = i;  
                for (int j = i+i; j <= n; j += i) {  
                    first_factor[j] = i;  
                }  
            }  
        }  
           
        // f(p*q) = f(p) * f(q) , because f(i) = i ^ (something)  
        vector<long> dp(n + 1, 1LL );  
        long sum = 0;  
        for (int i = 1; i <= n; i++) {  
            if (first_factor[i] == i) {  
                dp[i] = get_ith_element(i,k,m);  
            } else {  
                dp[i] = (dp[first_factor[i]] * dp[i / first_factor[i]]) % m;  
            }  
            sum += dp[i];  
        }  
        return (int)(sum % m);  
    } 
};

/*
return sum_{i=1}^n i^{2^k - 1} mod m
n will be between 1 and 1,000,000, inclusive.
k will be between 1 and 400, inclusive.
m will be between 2 and 1,000,000,000, inclusive.
*/