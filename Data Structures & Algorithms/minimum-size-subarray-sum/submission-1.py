class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        minLength = 100001
        sum = 0
        while r < len(nums):
            
            while r < len(nums) and sum < target:
                sum+= nums[r]
                r+=1
            if sum >= target:
                minLength = min(minLength, r-l)
            while l < r and sum >= target:
                sum-=nums[l]
                l+=1
                if sum >= target:
                    minLength = min(minLength, r-l)
                    
        if minLength == 100001:
            return 0
        else:
            return minLength