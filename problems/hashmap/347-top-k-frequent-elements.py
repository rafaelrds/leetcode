from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [set() for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in nums:
            frequency[count[num]].add(num)

        res = []
        for i in range(len(frequency) - 1, -1, -1):
            while len(frequency[i]) and k:
                res.append(frequency[i].pop())
                k -= 1
        return res
