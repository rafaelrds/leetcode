class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        N = len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                # we are in the left sorted portion
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                # we are in the right sorted portion
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[right]:
                    right = mid -1
                else: left = mid + 1
        return -1
