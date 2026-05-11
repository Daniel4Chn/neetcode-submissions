class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        runningProduct = 1
        for i in range(len(nums)):
            runningProduct *= nums[i]
            prefix[i] = runningProduct
        runningProduct = 1
        for j in range(len(nums)-1,-1,-1):
            runningProduct *= nums[j]
            postfix[j] = runningProduct
        output = [0] * len(nums)
        for i in range(len(output)):
            if i == 0:
                output[i] = postfix[i+1]
            else:
                if i == len(nums)-1:
                    output[i] = prefix[i-1]
                else:
                    output[i] = prefix[i-1]*postfix[i+1]
        return output
        