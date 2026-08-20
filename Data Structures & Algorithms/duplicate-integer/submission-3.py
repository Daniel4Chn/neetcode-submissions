class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNums = set()
        for i in range(len(nums)):
            if nums[i] in setOfNums:
                return True
            setOfNums.add(nums[i])
        return False