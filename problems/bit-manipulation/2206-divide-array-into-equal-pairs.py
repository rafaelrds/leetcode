import operator
from functools import reduce

class Solution:
    def divideArray(self, nums):
        arr = [1 << num for num in nums]
        return reduce(operator.xor, arr, 0)==0
