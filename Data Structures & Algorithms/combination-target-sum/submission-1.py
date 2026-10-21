class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #choose current number if current sum in array is less than target value
        
        #if current sum in array is equal to target value, append that number and pop the array and move pointer right one more to see if there are other options that might lead to the same sum 

        #if current sum is greater than target value, pop the array number and move pointer right more to see if there are other options that miught lead to the target sum
        options = []
        arr = []
        def dfs(i, sumTotal):
            if i >= len(nums) or sumTotal > target:
                return
            if sumTotal == target:
                print("hello")
                options.append(arr.copy())
                return
            
            arr.append(nums[i])
            dfs(i, sumTotal + nums[i])
            arr.pop()
            dfs(i+1, sumTotal)
        dfs(0, 0)
        return options

