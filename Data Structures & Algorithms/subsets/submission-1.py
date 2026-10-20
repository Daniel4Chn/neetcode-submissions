class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        #my initial thought process with this subsets question is to have a res array where i store all of the valid subsets of the array nums
        #i want to traverse the decision tree so im given the array nums and i want to iterate through the decision
        #for any given number, you have the option to choose it or exclude it so when i start with 1, i can choose 2 or exclude 2 if i choose 2, i can choose 3 or exclude three and then once i hit the end, i can pop back up to one and choose 3 and then i move to the next number

        def dfs(i,arr):
            if i >= len(nums):
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()
            dfs(i+1,arr)
            
        dfs(0,[])
        return res