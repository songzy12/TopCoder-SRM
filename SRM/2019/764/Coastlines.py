class Coastlines:
    def longest(self, map):
        met = set()
        ans = 0
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '.':
                    continue
                if (i, j) in met:
                    continue
                met.add((i, j))

                def bfs(x0, y0):
                    q = [(x0, y0)]
                    temp_ans = 0
                    while q:
                        x, y = q.pop(0)
                        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            if 0 <= x+dx < len(map) and 0 <= y+dy < len(map[i]) and \
                                    map[x+dx][y+dy] == 'X' and (x+dx, y+dy) not in met:
                                met.add((x+dx, y+dy))
                                q.append((x+dx, y+dy))

                        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            if x + dx < 0 or x + dx >= len(map):
                                temp_ans += 1
                                continue
                            if y + dy < 0 or y + dy >= len(map[0]):
                                temp_ans += 1
                                continue
                            if map[x+dx][y+dy] == '.':
                                temp_ans += 1
                                continue
                    return temp_ans

                temp_ans = bfs(i, j)                
                if temp_ans > ans:
                    ans = temp_ans
        return ans
