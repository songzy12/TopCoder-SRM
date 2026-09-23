class Restrictions:
    def exist(self, n, m, type, l, r, val):
        max_ = [None for i in range(n)]
        min_ = [None for i in range(n)]
        
        for i in range(m):
            if type[i] == 1:
                for j in range(l[i], r[i]+1):
                    if min_[j] == None:
                        min_[j] = val[i]
                    else:
                        min_[j] = max(min_[j], val[i])
            else:
                for j in range(l[i], r[i]+1):
                    if max_[j] == None:
                        max_[j] = val[i]
                    else:
                        max_[j] = min(max_[j], val[i])
        res = [1 for i in range(n)]
        # print(min_)
        # print(max_)
        for i in range(n):
            if max_[i] == None and min_[i] == None:
                continue
            if max_[i] == None:
                res[i] = min_[i]
                continue
            if min_[i] == None:                
                res[i] = 1
                continue

            if min_[i] <= max_[i]:
                res[i] = min_[i]
            else:
                return (-1, )
        return tuple(res)

n = 2
m = 3
type = [1, 2, 2]
l = [0, 1, 0]
r = [1, 1, 0]
val = [3, 4, 4]
# print(Restrictions().exist(n, m, type, l, r, val))