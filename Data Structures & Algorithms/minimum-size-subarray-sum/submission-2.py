class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        
        minLength = float('inf')
        sum = 0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum >= target:
                minLength = min(r-l+1,minLength)
                sum-=nums[l]
                l+=1
        
        if minLength == float('inf'):
            return 0
        else:
            return minLength