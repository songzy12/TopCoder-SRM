class RectangleHunt:
    def largest(self, x, y):
        ans = -1
        m = set([(x[i], y[i]) for i in range(len(x))])

        def compute_area(i0, j0, k0, x, y):
            triple = [(x[t], y[t]) for t in [i0, j0, k0]]
            for t in range(3):
                mid = triple[t]
                side = [triple[x] for x in range(3) if x != t]

                x0, y0 = mid
                x1, y1 = side[0]
                x2, y2 = side[1]

                if (x1 - x0)*(x2 - x0) + (y1 - y0)*(y2 - y0) == 0:
                    break
            else:
                return -1

            x4 = x1 + x2 - x0
            y4 = y1 + y2 - y0
            if (x4, y4) not in m:
                return -1
            import math
            return math.sqrt((x1 - x0)**2 + (y1 - y0)**2) * \
                math.sqrt((x2 - x0)**2 + (y2 - y0)**2)

        for i in range(len(x)):
            for j in range(i+1, len(x)):
                for k in range(j+1, len(x)):
                    ans = max(ans, compute_area(i, j, k, x, y))
        return ans # NOTE: the indention will affect the result!


x = [0, 1, 2, 3, 4, 4, 3]
y = [0, 0, 0, 0, 0, 1, 1]
print(RectangleHunt().largest(x, y))
