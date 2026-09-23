class LongJump2:
    def countNewLeaders(self, N, jumpLenghts):
        cur = None
        cnt = 0
        max_length = -1
        for i in range(3):
            for j in range(N):
                length = jumpLenghts[i*N+j]
                if length > max_length:
                    max_length = length
                    if j != cur:
                        cur = j
                        cnt += 1
        return cnt
            