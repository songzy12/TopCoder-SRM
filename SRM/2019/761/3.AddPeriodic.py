class AddPeriodic:
    def add(self, A, B):
        def str2num(s):
            index_dot = 0
            index_left = 0
            index_right = 0
            i = 0
            while i < len(s) and s[i] != '.':
                i += 1
            index_dot = i
            i + 1
            while i < len(s) and s[i] != '(':
                i += 1
            index_left = i
            index_right = len(s) - 1

            temp1 = int(s[:index_dot] + s[index_dot+1:index_left] +
                        s[index_left+1:index_right])
            temp2 = int(s[:index_dot] + s[index_dot+1:index_left] +
                        s[index_left+1:index_right] * 2)
            x = 10**(index_left - index_dot - 1 + index_right -
                     index_left - 1) - 10**(index_left - index_dot - 1)
            y = temp2 - temp1
            import math
            g = math.gcd(x, y)
            return x // g, y // g

        def add(a, b):
            x1, y1 = a
            x2, y2 = b
            x = x1 * y2 + x2 * y1
            y = y1 * y2
            import math
            g = math.gcd(x, y)
            return x // g, y // g

        def num2str(n):
            x, y = n
            res = ""
            # TODO: convert
            return res

        return num2str(add(str2num(A), str2num(B)))
