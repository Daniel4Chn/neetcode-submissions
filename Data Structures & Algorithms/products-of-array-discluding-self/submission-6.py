class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [1]*len(nums)
        postfixArr = [1]*len(nums)
        runningProduct = 1
        for i in range(1,len(nums)):
            prefixArr[i] = prefixArr[i-1]*nums[i-1]
        
        for j in range(len(nums)-2,-1,-1):
            postfixArr[j] = postfixArr[j+1]*nums[j+1]
        
        res = [1]*len(nums)
        for k in range(len(nums)):
            res[k] = prefixArr[k]*postfixArr[k]
        
        return res
