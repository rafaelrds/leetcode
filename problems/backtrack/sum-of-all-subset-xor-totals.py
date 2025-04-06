from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0

        def backtrack(i, curr):
            # base case
            if i == len(nums):
                self.res += curr
                return

            # pick nums[i]
            backtrack(i + 1, curr ^ nums[i])
            # do not pick nums[i]
            backtrack(i + 1, curr)

        backtrack(0, 0)
        return self.res
