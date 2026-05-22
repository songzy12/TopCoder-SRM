# ## Problem Statement
#
# All letters in this problem are uppercase English letters: 'A' to 'Z'. In other words, the 26 letters one can find on a standard US keyboard.
#
# You are given the string good. The letters that appear (one or more times) in good are good. The letters that don't appear in good are bad.
# You are also given the integers N and G.
# We are looking for a string with the following properties:
# - It consists of exactly N letters.
# - All those letters are mutually distinct.
# - Exactly G letters in this string are good.
#
# If such strings exist, construct and return any one such string. Otherwise, return an empty string.
#
# ## Constraints
# - good will have between 0 and 50 characters, inclusive.
# - Each character in good will be from 'A'-'Z'.
# - N will be between 1 and 26, inclusive.
# - G will be between 0 and N, inclusive.

import string


class GoodLetters:

    def construct(self, good, N, G):
        count_good = G
        count_bad = N - G
        letters_good = set(good)
        letters_bad = set(string.ascii_uppercase) - letters_good
        if len(letters_good) < count_good or len(letters_bad) < count_bad:
            return ''
        return ''.join(letters_good)[:count_good] + ''.join(
            letters_bad)[:count_bad]


good_letters = GoodLetters()
print(good_letters.construct(good="AEIOU", N=10, G=3))
