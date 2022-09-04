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
        # The final goal is to swap all elements from A to B, vice versa.
        # The invariant would be: after each loop i, the elements of A[...i] and B[...i] are sorted.

        A_with_index = []
        B_with_index = []
        for i in range(N):
            A_with_index.append([A[i], i])
            B_with_index.append([B[i], i])
        A_with_index.sort()
        B_with_index.sort()

        A_cur_index = [-1 for i in range(N)]
        A_target_index = [-1 for i in range(N)]
        B_cur_index = [-1 for i in range(N)]
        B_target_index = [-1 for i in range(N)]
        for i in range(N):
            # A_with_index[i][-1] = j means the ith largest element is now in position j.
            j = A_with_index[i][-1]
            # A_cur_index[i] = j means the ith largest element is now in position j.
            A_cur_index[i] = j
            # A_cur_index[j] = i means the element now in position j should end up in position i.
            A_target_index[j] = i
            j = B_with_index[i][-1]
            B_cur_index[i] = j
            B_target_index[j] = i
        # print(f"A: {A}")
        # print(f"B: {B}")
        # print(f"A_cur_index: {A_cur_index}")
        # print(f"A_target_index: {A_target_index}")
        # print(f"B_cur_index: {B_cur_index}")
        # print(f"B_target_index: {B_target_index}\n")

        # A_cur_index[i] = j means the ith largest element are now in position j.
        # which means A[j] is the ith largest element.
        res = []
        for i in range(N):
            j = A_cur_index[i]
            k = B_cur_index[i]
            # print(f"i={i}, j={j}, k={k}")
            if j == i and k == i:
                res.extend([j, k])
                # A[i], B[i] = B[i], A[i]
            elif j == i and k != i:
                res.extend([j, i])
                res.extend([i, k])
                tmp = B_target_index[i]
                B_cur_index[tmp] = k
                B_target_index[k] = tmp
                # A[i], B[i], B[k] = B[k], A[i], B[i]
            elif j != i and k == i:
                res.extend([i, k])
                res.extend([j, i])
                tmp = A_target_index[i]
                A_cur_index[tmp] = j
                A_target_index[j] = tmp
                # A[i], A[j], B[i] = B[i], A[i], A[j]
            else:
                res.extend([j, i])
                res.extend([i, k])
                res.extend([j, k])
                tmp = A_target_index[i]
                A_cur_index[tmp] = j
                A_target_index[j] = tmp
                tmp = B_target_index[i]
                B_cur_index[tmp] = k
                B_target_index[k] = tmp
                # A[i], A[j], B[i], B[k] = B[k], A[i], A[j], B[i]
            # print(f"A: {A}")
            # print(f"B: {B}")
            # print(f"A_cur_index: {A_cur_index}")
            # print(f"A_target_index: {A_target_index}")
            # print(f"B_cur_index: {B_cur_index}")
            # print(f"B_target_index: {B_target_index}")
            # print(f"res: {res}\n")
        return res


sort_two_arrays = SortTwoArrays()
# # case 0
# N = 3
# A = [10, 20, 30]
# B = [10, 20, 30]
# print(sort_two_arrays.twoSorts(N, A, B))  # [0, 0]
# case 1
N = 5
A = [10, 11, 12, 22, 14]
B = [20, 21, 13, 23, 24]
print(sort_two_arrays.twoSorts(N, A, B))  # [3, 2]
# # case 2
# N = 5
# A = [10, 50, 60, 30, 80]
# B = [20, 70, 99, 90, 40]
# print(sort_two_arrays.twoSorts(N, A, B))  # [1, 2, 3, 1, 1, 4]
# # case 3
# N = 4
# A = [1, 2, 90, 2]
# B = [60, 70, 80, 2]
# print(sort_two_arrays.twoSorts(N, A, B))  # [2, 3]
