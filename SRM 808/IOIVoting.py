# https://codeforces.com/blog/entry/92172
# 
# Imagine the difference in votes as the "capacity" of a directed edge from winner to loser. 
# S(A,B) is then simply the biggest capacity of a path from A to B.
# One easy way to compute all S(A,B) is Floyd-Warshall.
class IOIVoting:
    def winners(self, N, votes):
        pass