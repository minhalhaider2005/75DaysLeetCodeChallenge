class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            row = mid // n
            col = mid % n
            
            value = matrix[row][col]
            
            if value == target:
                return True
            elif value < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False