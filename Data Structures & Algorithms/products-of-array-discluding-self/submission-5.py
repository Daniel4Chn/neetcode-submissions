class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [1] * len(nums)
        postfixSum = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1]*nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            postfixSum[i] = postfixSum[i+1]*nums[i+1]
        
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefixSum[i]*postfixSum[i]
        return res
        
        
