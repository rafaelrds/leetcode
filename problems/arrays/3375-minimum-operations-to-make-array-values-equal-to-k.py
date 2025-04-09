from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique_values = set()
        for num in nums:
            if num > k:
                unique_values.add(num)
            if num < k:
                return -1
        
        return len(unique_values)        
