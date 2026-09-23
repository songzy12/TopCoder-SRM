# Your task is to write a program in this model with the following property:
# if the value M at the beginning of the program has the value (2^x * 3^y * 7),
# the program must eventually terminate and when it does,
# the final value M must be equal to 5^{x*y}.
#
# At most 25 instructions (i.e., fractions in your program).
# At most 6,000 steps of execution for any valid starting M with x, y <= 20.
# Each numerator and denominator must be a positive integer that fits into a signed 32-bit integer variable.
# The value of M must never exceed 10^2500.
#
# https://en.wikipedia.org/wiki/FRACTRAN
#
# Note variable v7 is already used here, thus we want to clear this variable by (1, 7).
# Then we substitute v7 with v19 in the solution of FRACTRAN.


class IOIWeirdModel2:

    def program(self, L):
        return (1, 7, 5 * 19 * 13, 3 * 11, 11, 13, 1, 11, 3, 19, 11, 2, 1, 3)
