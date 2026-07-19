class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = m - 1
        if target >= matrix[j][0]:
            i = j
        else:
            while i < j - 1:
                mid = (i + j) // 2
                if matrix[mid][0] > target:
                    j = mid
                elif matrix[mid][0] < target:
                    i = mid
                else:
                    return True
        
        k = 0
        l = n - 1

        if matrix[i][0] == target:
            return True
        
        while k < l:
            mid = (k + l) // 2
            if matrix[i][mid] > target:
                l = mid - 1
            elif matrix[i][mid] < target:
                k = mid + 1
            else:
                return True
        if matrix[i][k] == target:
            return True

        return False

        

