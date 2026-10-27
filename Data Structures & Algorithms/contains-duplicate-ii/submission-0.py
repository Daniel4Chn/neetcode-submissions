class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dictOfValues = {}
        for i in range(len(nums)):
            if nums[i] not in dictOfValues:
                dictOfValues[nums[i]] = i
            elif nums[i] in dictOfValues:
                if (i - dictOfValues[nums[i]]) <= k:
                    return True
                else:
                    dictOfValues[nums[i]] = i
        return False