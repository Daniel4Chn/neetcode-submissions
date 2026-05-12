class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        setOfAllNums = set()
        for num in nums:
            setOfAllNums.add(num)
        
        setOfValidNums = set()
        for num in nums:
            if num-1 not in setOfAllNums:
                setOfValidNums.add(num)
        
        LCS = 1
        for num in setOfValidNums:
            currentStreak = 1
            currNum = num
            while currNum + 1 in setOfAllNums:
                currNum = currNum + 1
                currentStreak +=1
                LCS = max(LCS, currentStreak)
        return LCS

