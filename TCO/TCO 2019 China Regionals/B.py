class SaturdayNightStay:
    def countOptions(self, firstDay, firstMonth, lastDay, lastMonth):
        def get_day_cnt(month, day):
            # 是第几天
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            cnt = 0
            for t in range(month - 1):
                cnt += months[t]
            cnt += day
            return cnt

        def get_weekday(cnt):
            # 1, 1 Tuesday
            cnt %= 7
            return (2 + cnt - 1) % 7

        cnt1 = get_day_cnt(firstMonth, firstDay)
        cnt2 = get_day_cnt(lastMonth, lastDay)

        head = 0
        day = cnt1
        while get_weekday(day) != 0:
            day += 1
            head += 1
            if day > cnt2:
                break

        tail = 0
        day = cnt2
        while get_weekday(day) != 6:
            day -= 1
            tail += 1
            if day < cnt1:
                break

        mid = cnt2 - cnt1 + 1 - head - tail
        # there may be no mid
        # print(head, mid, tail)
        res = head * (mid + tail)
        for i in range(1, mid + 1):
            res += (mid - i) // 7 * 7 + tail
        return res


firstDay = 31
firstMonth = 1
lastDay = 1
lastMonth = 2
print(SaturdayNightStay().countOptions(firstDay, firstMonth, lastDay, lastMonth))
