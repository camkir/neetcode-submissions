class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set = set(nums)
        if len(Set) != len(nums):
            return True
        else: 
            return False
         