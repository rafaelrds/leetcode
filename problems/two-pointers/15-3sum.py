from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums) - 2):
            # skip numbers that are already visited
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    # add sorted triplet to result
                    triplet = [nums[i], nums[l], nums[r]]
                    res.append(triplet)

                    # skip repeated numbers on left
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l +=1
                    
                    # skip repeated numbers on right
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif summ > 0:
                    r -= 1
                else:
                    l += 1

        return res
