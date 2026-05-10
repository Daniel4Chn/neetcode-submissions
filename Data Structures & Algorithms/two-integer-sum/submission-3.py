class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapOfValues = {}
        for i in range(len(nums)):
            targetToReach = target-nums[i]
            if targetToReach in mapOfValues:
                return [mapOfValues[targetToReach], i]
            mapOfValues[nums[i]] = i
        return None
        