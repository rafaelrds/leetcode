class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        N = len(nums)
        left = 0
        right = len(nums) - 1
        # find pivot
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # pivot will be at right!
        start = left
        left = 0
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            index = (mid + start) % N 
            if nums[index] == target:
                return index
            elif nums[index] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1