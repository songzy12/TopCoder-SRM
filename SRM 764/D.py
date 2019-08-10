class FourSquareSum:
    def DivideByTwo(self, a, b, c, d):
        odd = []
        even = []
        for t in [a, b, c, d]:
            if t % 2 == 1:
                odd.append(t)
            else:
                even.append(t)
        if len(odd) == 2:
            x = (odd[0] + odd[1]) / 2
            y = abs((odd[0] - odd[1]) / 2)
            s = (even[0] + even[1]) / 2
            z = abs((even[0] - even[1]) / 2)
        elif len(odd) == 4:
            s = (odd[0] + odd[1]) / 2
            z = abs((odd[0] - odd[1]) / 2)
            
            x = (odd[2] + odd[3]) / 2
            y = abs((odd[2] - odd[3]) / 2)
        else:
            s = (even[0] + even[1]) / 2
            z = abs((even[0] - even[1]) / 2)
            
            x = (even[2] + even[3]) / 2
            y = abs((even[2] - even[3]) / 2)
        return x, y, z, s