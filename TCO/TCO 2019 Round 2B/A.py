# 先数出总共又多少 小于、等于、大于
# 以及每个人有多少 小于、等于、大于

# 然后根据小于、等于、大于数来进行判断

# 然后将每个人进行排序


class MedianFaking:
    def minimize(self, F, M, data, goal):
        data_ = []
        total = [0, 0, 0]

        for i in range(F):
            cur = data[i*M:i*M+M]
            list_ = [filter(lambda x: x < goal, cur), filter(
                lambda x: x == goal, cur), filter(lambda x: x > goal, cur )]
            cur_cnt = list(map(lambda x: len(list(x)), list_))
            data_.append(cur_cnt)
            for t in range(3):
                total[t] += cur_cnt[t]
        # print(total)
        # print(data_)

        if total[0]+total[1] < (len(data)+1) // 2:
            total_change = (len(data)+1) // 2 - (total[0]+total[1])
            data_.sort(key=lambda x: x[-1], reverse=True)
            cur_change = 0
            cur_cnt = 0
            for d in data_:
                if cur_change >= total_change:
                    break
                cur_cnt += 1
                cur_change += d[-1]
            return cur_cnt, total_change
        elif total[0] < (len(data)+1) // 2:
            return 0, 0
        else:            
            total_change = total[0] - ((len(data)+1) // 2 -1)
            data_.sort(key=lambda x: x[0], reverse=True)
            cur_change = 0
            cur_cnt = 0
            for d in data_:
                if cur_change >= total_change:
                    break
                cur_cnt += 1
                cur_change += d[0]
            return cur_cnt, total_change



# F = 5
# M = 5
# data = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 25, 24, 23,
#         22, 21, 18, 17, 16, 19, 20, 11, 12, 13, 14, 15]
# goal = 8
# print(MedianFaking().minimize(F, M, data, goal))
