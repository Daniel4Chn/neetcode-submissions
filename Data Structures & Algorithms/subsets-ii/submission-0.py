class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currentArr = []
        res = []

        def backTrack(index):
            res.append(currentArr[:])

            if len(currentArr) == len(nums) or index > len(nums):
                return
            
            for i in range(index, len(nums)):
                if i < len(nums) and i > index and nums[i] == nums[i-1]:
                    continue
                currentArr.append(nums[i])
                backTrack(i+1)
                currentArr.pop()

            


        backTrack(0)
        return res