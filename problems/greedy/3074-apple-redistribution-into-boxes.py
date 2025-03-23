from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)

        total_apples = sum(apple)
        for i, c in enumerate(capacity):
            total_apples -= c
            if total_apples <= 0:
                return i + 1
