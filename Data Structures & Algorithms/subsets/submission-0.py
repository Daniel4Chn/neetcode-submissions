class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        currentSubset = []

        def pathOfNums(start):

            result.append(currentSubset[:])

            if len(currentSubset) == len(nums):
                return
            
            for i in range(start, len(nums)):
                currentSubset.append(nums[i])
                pathOfNums(i+1)
                currentSubset.pop()

            
        pathOfNums(0)
        return result
        
