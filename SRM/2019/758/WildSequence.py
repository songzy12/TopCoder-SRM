class WildSequence:
    def construct(self, head, rest):
        if not rest:
            # NOTE: here
            return [head]
        rest = list(rest)
        rest.sort()
        _min = rest[0]
        if _min > head:
            rest = rest[::-1]
        res = [head]
        i = 0
        j = len(rest) - 1
        while i < j:
            res.append(rest[i])
            res.append(rest[j])
            i += 1
            j -= 1
        if i == j:
            # NOTE: here
            res.append(rest[i])
        return tuple(res)

head = 20
rest = (10,30,40)
print(WildSequence().construct(head, rest))