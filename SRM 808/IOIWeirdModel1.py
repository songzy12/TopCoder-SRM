# One easy-to-implement idea to find the median of five numbers is "while you can decrement at least three of a,b,c,d,e, decrement all you can and increment the output".
import itertools


class IOIWeirdModel1:
    def add_permutation(self, origin, dom, res):
        indicator = [2, 3, 5, 7, 11]
        visited = set()
        for permutation in itertools.permutations(origin, 5):
            prod = 1
            for x, y in zip(indicator, permutation):
                if y:
                    prod *= x
            if prod in visited:
                continue
            visited.add(prod)
            res.append(dom)
            res.append(prod)

    def program(self, L):
        res = []
        self.add_permutation([1, 1, 1, 1, 1], 47, res)
        self.add_permutation([1, 1, 1, 1, 0], 47, res)
        self.add_permutation([1, 1, 1, 0, 0], 47, res)
        self.add_permutation([1, 1, 0, 0, 0], 1, res)
        self.add_permutation([1, 0, 0, 0, 0], 1, res)
        return tuple(res)


if __name__ == "__main__":
    res = IOIWeirdModel1().program(2)
    print(len(res))
    print(res)