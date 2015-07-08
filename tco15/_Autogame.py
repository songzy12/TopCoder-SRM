from time import clock, sleep
class Autogame:
    def wayscnt(self, a, K):
        N = len(a)
        count = 0
        for i in range(0, 2**N):
            temp = bin(i)
            temp2 = [int(i) for i in str(temp)[2:].rjust(N,'0')]
            # print(str(temp)[2:].rjust(N,'0'), temp2)
            good = True
            for l in range(K):
                b = list(a)
                for j in range(len(a)):
                    if temp2[j]==0:
                        b[j] = None
                for j in range(len(a)):
                    if b[j]!=None:
                        temp2[j]-=1
                for j in range(len(a)):
                    if b[j]!=None:
                        temp2[b[j]-1]+=1
                if max(temp2) > 1:
                    good = False
                    break
            if good:
                count += 1
        return count
# also do not use python on TC
a = (23, 11, 9, 23, 1, 33, 40, 29, 33, 14, 27, 21, 36, 10, 19, 27, 43, 41, 17, 16, 17, 43,
     24, 11, 34, 43, 1, 16, 22, 42, 27, 9, 21, 27, 10, 27, 26, 29, 10, 14, 31, 25, 12, 6)
K = 8
##a = (5, 10, 19, 12, 21, 13, 11, 6, 2, 5, 21, 21, 1, 17, 9, 4, 5, 11, 5, 17, 5, 2, 6, 1)
##K = 2
##a = (1,2,3)
##K = 5
##a = (1,1,1)
##K = 1
##a =(2,1)
##K = 42
##a =(2,3,4,3)
##K = 3
##a =(4,4,3,2,1)
##K = 3
print(Autogame().wayscnt(a, K))
