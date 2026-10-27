class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lengthOfArr = len(nums)
        for i in range(lengthOfArr, lengthOfArr*2):
            nums.append(nums[i-lengthOfArr])
        return nums