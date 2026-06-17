class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setOfNums = set()
        for i in nums:
            if i in setOfNums:
                return i
            setOfNums.add(i)
        