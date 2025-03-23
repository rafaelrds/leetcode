from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        write = len(res) - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                res[write] = nums[right] ** 2
                right -= 1
            else:
                res[write] = nums[left] ** 2
                left += 1
            write -= 1
        return res

