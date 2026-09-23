# ## Problem Statement
# The International Olympiad in Informatics (IOI) is currently in progress. To honor this competition, our problems for this round have IOI-flavored stories.
#
# When taking an informal vote to choose among N options (numbered from 0 to N-1), the General Assembly (GA) of the IOI sometimes uses a voting system that allows the voters to express preferences.
# First, the votes are collected. The output of these votes is an N times N matrix: for each pair of options (i, j) the number p[i,j] of people who prefer i over j. You are given the contents of this matrix in the tuple (integer) votes. More precisely, votes[i*N+j] = p[i,j] is the number of voters who like option i more than option j.
# Note that not everyone expressed their preferences on all options, so the values in votes can be arbitrary (except for the main diagonal which is guaranteed to contain zeros). In particular, the preferences of the voters are not necessarily transitive.
# The results of the election are evaluated in a sequence of steps, as explained below.
#
# We say that voters prefer option A over option B if p[A,B] > p[B,A].
# We say that option A can defeat option B if there is a sequence C1 = A, C2, ..., C(k-1), Ck = B of options such that voters prefer C1 over C2, C2 over C3, ..., and C(k-1) over Ck. The sequence A = C1, C2, ..., Ck = B is called an argument that A can defeat B. The argument can be arbitrarily long.
# Note that sometimes one argument shows that A can defeat B but there can also be another argument that shows that B can defeat A.
#
# The strength of direct preference of option A over option B is equal to p[A,B] - p[B,A]: the difference between the number of votes "A is better than B" and votes "B is better than A".
# The strength of an argument is the minimum strength of direct preferences along the sequence: that is, the minimum over all valid i of the strength of the direct preference of Ci over C(i+1).
#
# For any two options A, B, let S(A,B) be the strength of the strongest argument that A can defeat B -- i.e., the maximum of strengths of all arguments that show that A can defeat B. If there are no such arguments, S(A,B) is defined to be zero.
# We say that option A is at least as powerful as option B if S(A,B) >= S(B,A).
# We say that option A is a potential winner if A is at least as powerful as each of the other N-1 options.
#
# Return a sequence of all potential winners. The sequence must be sorted in ascending order.
#
# ## Constraints
# - N will be between 1 and 50, inclusive.
# - votes will have exactly N*N elements.
# - Each element of votes will be between 0 and 9,999, inclusive.
# - For each i, votes[i*N+i] will be 0.


# Imagine the difference in votes as the "capacity" of a directed edge from winner to loser.
# S(A,B) is then simply the biggest capacity of a path from A to B.
# One easy way to compute all S(A,B) is Floyd-Warshall.
class IOIVoting:

    def winners(self, N, votes):
        pass