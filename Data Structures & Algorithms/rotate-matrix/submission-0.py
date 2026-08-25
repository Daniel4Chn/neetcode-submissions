class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #find transpose of the matrix and then reverse the rows

        

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp
        
        for i in range(len(matrix)):
            j = 0
            k = len(matrix[0])-1
            while j < k:
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][k]
                matrix[i][k] = temp
                j+=1
                k-=1
        
        
        
        
        