class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapOfVals = dict()
        for i in range(len(nums)):
            if target-nums[i] in mapOfVals:
                return [mapOfVals[target-nums[i]], i]
            mapOfVals[nums[i]] = i
        