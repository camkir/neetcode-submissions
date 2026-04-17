class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            delta = target - n
            if delta in prevMap:
                return [prevMap[delta], i]
            prevMap[n] = i