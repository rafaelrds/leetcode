import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(-num)
        heapq.heapify(heap)
        for _ in range(k):
            ans = -heapq.heappop(heap)
        return ans
