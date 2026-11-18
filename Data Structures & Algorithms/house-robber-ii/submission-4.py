class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[1], max(nums[0], nums[-1]))

        cacheFirst = [0] * len(nums)
        cacheSecond = [0] * len(nums)
        cacheFirst[0] = nums[0]
        cacheFirst[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)-1):
            cacheFirst[i] = max(cacheFirst[i-1], nums[i]+cacheFirst[i-2])
        
        cacheSecond[1] = nums[1]
        cacheSecond[2] = nums[2]
        for i in range(2,len(nums)):
            cacheSecond[i] = max(cacheSecond[i-1], nums[i]+cacheSecond[i-2])
        
        print(cacheFirst)
        print(cacheSecond)
        return max(cacheSecond[-1], cacheFirst[-2])
        

        