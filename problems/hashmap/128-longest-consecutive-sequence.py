from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        res = 0
        for num in seen:
            if num - 1 not in seen:
                # we are at the start of a sequence
                cur = num
                while cur + 1 in seen:
                    cur += 1
                res = max(res, cur - num + 1)
        return res
