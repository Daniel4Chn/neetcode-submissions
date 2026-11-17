class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if i == 1:
                if nums[i] >= nums[i-1]:
                    continue
                else:
                    nums[i] = nums[i-1]
                    continue
            if nums[i] + nums[i-2] > nums[i-1]:
                nums[i] = nums[i] + nums[i-2]
            else:
                nums[i] = nums[i-1]
        return nums[-1]
            



