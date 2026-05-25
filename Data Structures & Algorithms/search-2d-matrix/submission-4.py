class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix)-1
        correctRow = 0

        while l <= r:
            correctRow = (l+r)//2
            if matrix[correctRow][len(matrix[0])-1] < target:
                l = correctRow+1
            elif matrix[correctRow][len(matrix[0])-1] == target:
                return True
            elif matrix[correctRow][len(matrix[0])-1] > target:
                if matrix[correctRow][0] < target:
                    break
                elif matrix[correctRow][0] > target:
                    r = correctRow-1
                else:
                    return True
        
            
        
        
        l = 0
        r = len(matrix[0])-1
        while l <= r:
            mid = (l+r)//2
            if matrix[correctRow][mid] > target:
                r = mid-1
            elif matrix[correctRow][mid] < target:
                l = mid+1
            else:
                return True
        return False
        