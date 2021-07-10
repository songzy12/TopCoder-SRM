# for each contestant i,
# the smallest score is day1[i] + day2[i]
# for other contestant j, the largest score is day1[j] + 300


class IOIGuaranteedPlace:
    def solve(self, N, day1scores, day2scores):
        scores = []
        for i in range(N):
            scores.append((day1scores[i] + day2scores[i], 1, i))
            scores.append((day1scores[i] + 300, 0, -1))
        scores.sort(reverse=True)
        # print(scores)
        res = [0 for i in range(N)]
        cnt = 0        
        for _, _, contestant in scores:
            if contestant == -1:
                cnt += 1
            else:
                if day2scores[contestant] == 300:
                    res[contestant] = cnt + 1
                else:
                    res[contestant] = cnt
        return res