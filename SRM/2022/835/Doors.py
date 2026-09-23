class UnionFind:

    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.size = {node: 1 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False

        # Optimized with path compression and union-by-size.
        if self.size[root1] < self.size[root2]:
            root1, root2 = root2, root1
        self.parent[root2] = root1
        self.size[root1] += self.size[root2]
        return True


class Doors:

    def build(self, plan):
        rows = len(plan)
        columns = len(plan[0])
        open_cells = {(row, column)
                      for row in range(rows)
                      for column in range(columns)
                      if plan[row][column] == "."}
        components = UnionFind(open_cells)
        door_cost = 0

        # Row-wise connections.
        for row in range(rows):
            for column in range(columns - 1):
                left = (row, column)
                right = (row, column + 1)
                if left not in open_cells or right not in open_cells:
                    continue
                if components.union(left, right):
                    door_cost += 1

        # Column-wise connections.
        for row in range(rows - 1):
            for column in range(columns):
                top = (row, column)
                bottom = (row + 1, column)
                if top not in open_cells or bottom not in open_cells:
                    continue
                if components.union(top, bottom):
                    door_cost += 2

        return door_cost


if __name__ == "__main__":
    plan = ["..", ".."]
    assert Doors().build(plan) == 4

    plan = [".#.#.#", "#.#.#.", ".#.#.#"]
    assert Doors().build(plan) == 0

    plan = [".#..", ".###"]
    assert Doors().build(plan) == 3

    plan = [".....", "...#.", ".....", "....."]
    assert Doors().build(plan) == 22
