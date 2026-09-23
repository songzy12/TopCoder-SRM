class Sunshine:
    def weatherReport(self, totalDays, rainyDays):
        cnt = (totalDays - rainyDays) // (rainyDays + 1)
        res = (totalDays - rainyDays) % (rainyDays + 1)
        # print(cnt, res)
        ans = ""
        for t in range(res):
            ans += "S" * (cnt + 1)
            ans += "R"
        for t in range(rainyDays - res):
            ans += "S" * cnt
            ans += "R"
        ans += "S" * cnt
        return ans

totalDays = 6
rainyDays = 1
print(Sunshine().weatherReport(totalDays, rainyDays))