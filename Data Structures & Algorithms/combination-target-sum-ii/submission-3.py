class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #unique combinations of candidates where chosen numbers sum to target
        #each element from candidates may only be chosen at most once from a combination
        #no duplicate combinations
        res = []
        arr = []
        
        candidates.sort()
        def dfs(i, sumValue):
            if sumValue == target:
                res.append(arr.copy())
                return
            if i >= len(candidates) or sumValue > target:
                return
            
           
            arr.append(candidates[i])
            dfs(i+1, sumValue+candidates[i])
            arr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, sumValue)


        dfs(0,0)
        return res