class PartitionArray:
    def positiveSum(self, a):
        if sum(a) > 0:
            return (len(a), )
        else:
            return (-1, )

a = (3,-7,8)
print(PartitionArray().positiveSum(a))