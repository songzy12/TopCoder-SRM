class TheUnexpectedSwap:
    def findExpectedResult(self, digits, prefN, seed):
        A = [seed]
        for i in range(1, digits):
            A.append((A[-1] * 1009 + 10009) % 100019)

        N = []
        for i in range(len(prefN)):
            N.append(int(prefN[i]))
        for i in range(len(prefN), digits):
            N.append(N[A[i] % i])

        N = N[::-1]

        def compute_E(N, n):
            res = 0
            temp = 0
            for i, t in enumerate(N):
                temp += t * 10**i
            res += temp * ((n-1)*(n-2)/2 - 1)
            temp = sum(N)
            res += temp * (10**n - 1) / 9
            res = res * 2 
            return res
        E = compute_E(N, digits)
        p = 10**9+7
        
        return E % p

digits = 6
prefN = "123"
seed = 47
print(TheUnexpectedSwap().findExpectedResult(digits, prefN, seed))