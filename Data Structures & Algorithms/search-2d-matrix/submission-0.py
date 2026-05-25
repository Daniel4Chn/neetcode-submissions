class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for n in range(len(matrix)):
            l = 0
            r = len(matrix[0])-1

            while l <= r:
                mid = (l+r)//2
                if matrix[n][mid] > target:
                    r = mid-1
                elif matrix[n][mid] < target:
                    l = mid+1
                else:
                    return True
        
        return False