class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        currentComb = []
        res = []
        sumOfComb = 0
        def combine(index):
            nonlocal sumOfComb
            if sumOfComb == target:
                res.append(currentComb[:])
                return
            
            if sumOfComb > target:
                return
            
            for i in range(index, len(nums)):
                currentComb.append(nums[i])
                sumOfComb += nums[i]    
                combine(i)
                sumOfComb -= currentComb.pop()
                

        combine(0)
        return res
