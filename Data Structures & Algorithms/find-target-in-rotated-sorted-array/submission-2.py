class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find split
        shifts = 0
        for i in range(len(nums)):
            if nums[i] < nums[i-1]:
                shifts = i
                break
    
        nums = nums[shifts:] + nums[:shifts]

        # binary search
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                index = (mid + shifts)%len(nums)
                break
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return index


        
        