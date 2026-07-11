class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        currentArr = []
        arrOfTruths = [False for i in range(len(nums))]
        res = []

        def generateArr():

            if len(currentArr) == len(nums):
                res.append(currentArr[:])
                return

            for i in range(len(nums)):
                if not arrOfTruths[i]:
                    arrOfTruths[i] = True
                    currentArr.append(nums[i])
                    generateArr()
                    currentArr.pop()
                    arrOfTruths[i] = False
                    

        generateArr()
        return res