class Similars:
    def similar(self, a, b):
        count = 0
        for i in range(10):
            if str(i) in str(a) and str(i) in str(b):
                count += 1
        return count
    def maxsim(self, L, R):
        result = 0
        for i in range(L, R):
            for j in range(i+1, R+1):
                temp = self.similar(i, j)
                if temp > result:
                    result = temp
        return result

# BF is not suitable, even for C
L, R = (12, 1021)
print(Similars().maxsim(L, R))
