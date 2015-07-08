# bugs in TopCoder for supporting python
# the points only depend on time passed and #submits
# notice the messages illuminated by batch test
# c++ also needs to submit the included header files
# do not spend too much time on the first question
# the correctness is only envalued during system test
# also the challenge process sees untested codes

class RandomPancakeStack:
    def aux(self, d, n, m):
        if n == 0:
            return 0
        result = 0
        for j in range(n):
            result += 1 / m * (d[j] + self.aux(d, j, m - 1))
        return result
    def expectedDeliciousness(self, d):
        return self.aux(d, len(d), len(d))
   

for d in ((1,1,1), [10, 20], [3, 6, 10, 9, 2], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
          [1,2,3,4,5,6,7,8,9,10], [1,1,1,1,1,1,1,1,1,1]):
    print(RandomPancakeStackDiv2().expectedDeliciousness(d))
            
