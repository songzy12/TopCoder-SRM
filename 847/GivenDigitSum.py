# https://community.topcoder.com/stat?c=problem_statement&pm=18055&rd=19638

"""
Given are small positive integers D and S.

Return the smallest positive integer with the following properties:

    It has exactly D digits.
    The sum of its digits is exactly S.
    The product of its digits is zero.

If no such integer exists, return -1 instead. 

Constraints
-	D will be between 1 and 18, inclusive.
-	S will be between 1 and 200, inclusive.
"""


class GivenDigitSum():
    def construct(self, D, S):
        return self.construct_result(self.construct_num_array(D - 1, S - 1))

    def construct_num_array(self, D, S):
        if S >= 9 * D:
            return []
        res = [0 for i in range(D)]
        index = len(res) - 1
        while S:
            if S > 9:
                res[index] = 9
                S -= 9
                index -= 1
            else:
                res[index] = S
                break
        return res

    def construct_result(self, num_array):
        if not num_array:
            return -1
        res = ""
        res += str(num_array[0] + 1)
        res += "0"
        for num in num_array[1:]:
            res += str(num)
        return int(res)
