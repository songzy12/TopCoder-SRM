class Pickaxe:
    def countWalls(self, maze):
        def get_wall(r, c, maze):
            res = set()
            q = [(r, c)]
            visited = set()
            while q:
                # print(q)
                cur = q.pop(0)
                visited.add(cur)
                x, y = cur
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    if x + dx < 0 or x + dx >= len(maze):
                        continue
                    if y + dy < 0 or y + dy >= len(maze[0]):
                        continue
                    if (x+dx, y+dy) in visited:
                        continue
                    # print(x+dx, y+dy, maze[x+dx][y+dy])
                    if maze[x+dx][y+dy] == '#':
                        res.add((x+dx, y+dy))
                    else:
                        q.append((x+dx, y+dy))
            return res
        a = get_wall(0, 0, maze)
        b = get_wall(len(maze)-1, len(maze[0])-1, maze)
        # print(a, b)
        return len(a.intersection(b))


maze = [
    "..#",
    ".#.",
    "#.."
]
print(Pickaxe().countWalls(maze))
