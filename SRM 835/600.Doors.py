# ## Problem Statement
#
# You are given the tuple (string) plan: the floor plan of a rectangular building. The floor of the building is divided into unit square cells. Some squares are rooms (denoted '.'), the remaining ones are walls (denoted '#').
#
# Two rooms are considered adjacent if they share a side.
# Building a door between two adjacent rooms in the same row of the plan costs 1. Building a door between two adjacent rooms in the same column of the plan costs 2.
#
# The initial plan of the architect of the building was to have a door between each pair of adjacent rooms. However, the times are rough and so you decided to save some money.
# A set of doors is called sufficient if it allows you to move inside the building as well as a full set of doors would. More formally, if it's possible to go from one room to another in a building that has the given floor plan and all possible doors, it must also be possible to go there (possibly using a longer path) in the building that has the same floor plan but only your set of doors built between them.
#
# Find and return the total cost of the cheapest sufficient set of doors for the given building.
#
# ## Constraints
# - plan will contain between 1 and 30 elements, inclusive.
# - Each element of plan will contain between 1 and 30 characters, inclusive.
# - All elements of plan will contain the same number of characters.
# - Each character in plan will be '.' or '#'.


class Doors:

    def __init__(self):
        self.parent = {}

    def build(self, plan):
        res = 0
        # In the first pass,
        # Connect adjacent cells in the same row.
        # During the process, use group to indicate which group a specific cell belongs to.
        for i in range(len(plan)):
            for j in range(len(plan[0])):
                self.parent[i, j] = (i, j)

        for i in range(len(plan)):
            for j in range(len(plan[0]) - 1):
                if plan[i][j] == '.' and plan[i][j + 1] == '.' and self._find(
                    (i, j)) != self._find((i, j + 1)):
                    self._union((i, j), (i, j + 1))
                    res += 1

        # In the second pass,
        # For each pair of vertical ajdacent cells, check whether the groups they belong to are already connected.
        # If not, add an vertical edge to connect them.
        # During the process, also merge the vertically connected groups to be the same group.
        # Test case: [".....", "...#.", ".....", "....."]
        connected = {}
        for i in range(len(plan) - 1):
            for j in range(len(plan[0])):
                if plan[i][j] == '.' and plan[i + 1][j] == '.' and self._find(
                    (i, j)) != self._find((i + 1, j)):
                    self._union((i, j), (i + 1, j))
                    res += 2
        return res

    def _union(self, node1, node2):
        p1 = self._find(node1)
        p2 = self._find(node2)
        self.parent[p2] = p1

    def _find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node


# case 0
plan = ["..", ".."]
assert (Doors().build(plan) == 4)
# case 1
plan = [".#.#.#", "#.#.#.", ".#.#.#"]
assert (Doors().build(plan) == 0)
# case 2
plan = [".#..", ".###"]
assert (Doors().build(plan) == 3)
# case 4
plan = [".....", "...#.", ".....", "....."]
assert (Doors().build(plan) == 22)
