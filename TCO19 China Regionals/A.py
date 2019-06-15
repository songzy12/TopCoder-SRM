class LuckyElevator:
    def actualFloor(self, buttonPressed):
        a = []
        for i in range(100000+1):
            if '4' in str(i):
                continue
            a.append(i)
        m = {}
        for i, j in enumerate(a):
            m[j] = i
        return m[buttonPressed]