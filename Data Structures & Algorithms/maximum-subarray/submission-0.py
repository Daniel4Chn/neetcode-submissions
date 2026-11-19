class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = nums[0]
        maxSum = max(maxSum, currSum)
        for i in range(1,len(nums)):
            currSum = max(nums[i], currSum+nums[i])
            maxSum = max(maxSum, currSum)
        
        return maxSum