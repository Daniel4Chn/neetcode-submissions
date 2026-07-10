class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        currentList = []
        res = []
        setOfCombinations = set()
        candidates.sort()
        sumOfList = 0
        def findCombs(index):
            nonlocal sumOfList
            if sumOfList > target:
                return 
            
            if sumOfList == target:
                res.append(currentList[:])
                return

            if index < len(candidates):
                for i in range(index, len(candidates)):
                    if i > index and candidates[i-1] == candidates[i]:
                        continue
                    currentList.append(candidates[i])
                    sumOfList += candidates[i]
                    findCombs(i+1)
                    value = currentList.pop()
                    sumOfList -= value
            
        findCombs(0)
        return res
