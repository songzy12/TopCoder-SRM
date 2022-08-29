# ## Problem Statement
#
# You are given the integer N and two arrays A and B, containing N elements each.
# Your task is to transform the two arrays into a state in which both arrays are sorted. (The elements of A must be in non-descending order, and the elements of B must also be in non-descending order.)
#
# You can only modify the arrays in one way: by swapping an element of A with an element of B.
#
# For the two given arrays, determine whether it's possible to reach the goal by performing at most 3*N swaps. If a solution exists, find any one valid sequence of at most 3*N swaps.
#
# Suppose that you found a sequence of K swaps, the i-th of which (for i=0..K-1) swaps the element number x[i] in A with the element number y[i] in B. Then, return the following tuple (integer): { x[0], y[0], x[1], y[1], ..., x[K-1], y[K-1] }.
# If there is no solution, return {-1}. That is, the return value is an array with a single element, and that element has the value -1.
#
# ## Constraints
# - N will be between 1 and 999, inclusive.
# - A and B will have N elements each.
# - Each element of A and B will be between 0 and 999, inclusive.
class SortTwoArrays:
    
    def twoSorts(self, N, A, B):
        # Reference: 
        # - https://www.geeksforgeeks.org/check-whether-we-can-sort-two-arrays-by-swapping-ai-and-bi/
        # - https://stackoverflow.com/questions/51675765/minimum-swaps-to-relative-sort-two-arrays
        # - https://leetcode.com/discuss/interview-question/397156/google-oa-2020-relative-sort
        # - https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss
        pass


sort_two_arrays = SortTwoArrays()
# case 0
N = 3
A = [10, 20, 30]
B = [10, 20, 30]
assert (sort_two_arrays.twoSorts(N, A, B) == [0, 0])
# case 1
N = 5
A = [10, 11, 12, 22, 14]
B = [20, 21, 13, 23, 24]
assert (sort_two_arrays.twoSorts(N, A, B) == [3, 2])
# case 2
N = 5
A = [10, 50, 60, 30, 80]
B = [20, 70, 99, 90, 40]
assert (sort_two_arrays.twoSorts(N, A, B) == [1, 2, 3, 1, 1, 4])
# case 3
N = 4
A = [1, 2, 90, 2]
B = [60, 70, 80, 2]
assert (sort_two_arrays.twoSorts(N, A, B) == [2, 3])
